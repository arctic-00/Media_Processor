
from moviepy.editor import * 
from PIL import Image
import os, shutil


PREFFERED_VIDEO_DURATION = 30
DESTINATION_FOLDER_NAME = "New_Art"



# Check if folder exists and if not make a new one
current_directory = os.getcwd()
dst_dir = current_directory + '\\' + DESTINATION_FOLDER_NAME
if not os.path.exists(dst_dir):
    os.mkdir(dst_dir)


# Get the list of all files in current folder
dirList = os.listdir()

# FUNCTION Remove videos from list that are already in DESTINATION_FOLDER_NAME
vids_in_new_folder = os.listdir(dst_dir)
def check_to_add_video(filename):
    duplicate = False
    for a_vid_in_new_folder in vids_in_new_folder:
        if ("longer_" + filename == a_vid_in_new_folder):
            duplicate = True
            
    if not duplicate:
        videos.append(filename)


# Separate video and img files different lists
print("\n\nSorting lists and removing videos that have already been lengthened from queue..")
videos = []
trad_imgs = []
webp_imgs = []
for i in range(len(dirList)):
    filename = dirList[i]
    file_type = os.path.splitext(filename)[1]
    
    if (file_type == ".mp4"):
        check_to_add_video(filename)        # Remove videos from list that are already in DESTINATION_FOLDER_NAME
    elif (file_type == ".webp"):
        webp_imgs.append(filename)
    elif (file_type != ".py" and len(file_type) != 0):
        trad_imgs.append(filename)
print("Done Sorting.")



# Lengthen videos and place in DESTINATION_FOLDER_NAME
i = 0
for name in videos:
    i += 1
    print("\nVideo %d of %d" %(i, len(videos)))
        
    clip = VideoFileClip(name)

    numOfReps = int(PREFFERED_VIDEO_DURATION / clip.duration) + 1
    clipList = numOfReps * [clip]
    mergedVid = concatenate_videoclips(clipList)
    vid_path_to_save = DESTINATION_FOLDER_NAME + '\longer_' + name
    mergedVid.write_videofile(vid_path_to_save, codec='libx264')
    

print("\n\nConverting and copying images..")
# Copy traditional image formats to New_Art (jpg, png)
for name in trad_imgs:
    src = current_directory + '\\' + name
    dst = current_directory + '\\' + DESTINATION_FOLDER_NAME + '\\' + name
    shutil.copy(src, dst)


# Convert webp images to jpg and move to New_Art
for name in webp_imgs:

    im = Image.open(name).convert("RGB")
    new_name = DESTINATION_FOLDER_NAME + '\\' + os.path.splitext(name)[0] + ".jpeg"
    im.save(new_name, 'jpeg', quality=90)


print("Done!")