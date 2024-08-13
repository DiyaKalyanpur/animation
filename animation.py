import bpy
from mathutils import Quaternion

# Set the total animation length (in seconds)
total_animation_length = 8  # 3 seconds for atria + 5 seconds for ventricles

# Set the frame rate
frame_rate = 24

# Calculate the total number of frames
total_frames = total_animation_length * frame_rate

# Set the scene end frame
bpy.context.scene.frame_end = total_frames

# Get the heart object (assuming it's named "Heart")
heart = bpy.data.objects["polySurface4"]

# Define the shape keys and their timings
shape_keys = {
    "LAC": {"start": 0, "end": 5 * frame_rate},
    "RAC": {"start": 0, "end": 5 * frame_rate},
    "LVC": {"start": 5 * frame_rate, "end": 10 * frame_rate},
    "RVC": {"start": 5 * frame_rate, "end": 10 * frame_rate}
}

# Animate the shape keys
for key_name, timing in shape_keys.items():
    if key_name in heart.data.shape_keys.key_blocks:
        shape_key = heart.data.shape_keys.key_blocks[key_name]
        
        # Set initial keyframe (shape key value = 0)
        shape_key.value = 0
        shape_key.keyframe_insert("value", frame=0)
        
        # Set keyframe at start of contraction (shape key value = 1)
        shape_key.value = 1
        shape_key.keyframe_insert("value", frame=timing["start"])
        
        # Set keyframe at end of contraction (shape key value = 1)
        shape_key.value = 1
        shape_key.keyframe_insert("value", frame=timing["end"])
        
        # Set final keyframe (shape key value = 0)
        shape_key.value = 0
        shape_key.keyframe_insert("value", frame=total_frames)

# Set interpolation to linear for all f-curves
for fc in heart.data.shape_keys.animation_data.action.fcurves:
    for kf in fc.keyframe_points:
        kf.interpolation = 'LINEAR'

print("Animation complete!")