# HW :1 -> 

# print('''Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.

# Twinkle, twinkle, little star,
# How I wonder what you are!

# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.

# Twinkle, twinkle, little star,
# How I wonder what you are!

# Then the traveler in the dark
# Thanks you for your tiny spark;
# He could not see which way to go,
# If you did not twinkle so.

# Twinkle, twinkle, little star,
# How I wonder what you are!

# In the dark blue sky you keep,
# And often through my curtains peep,
# For you never shut your eye
# Till the sun is in the sky.

# Twinkle, twinkle, little star,
# How I wonder what you are!''')

# HW:2 ->
import pyttsx3
audio = pyttsx3.init()
audio.say("Hello, I am good")
audio.runAndWait()

#HW:3  ->
import os
directory_path = "D:\Parikshit\Python"

contents = os.listdir(directory_path)
print(contents)