import os
import wave

# Specify the path to the folder with the input audio files
input_folder = 'input'
# Specify the path to the output audio files folder
output_folder = 'output'

# Sorting through all the files in the folder
for filename in os.listdir(input_folder):
    # Check that the file is a wav audio file
    if filename.endswith('.wav'):
        # Opening the audio file
        with wave.open(os.path.join(input_folder, filename), 'r') as file:
            # Reading the title
            params = file.getparams()
            # We determine the number of samples in the audio file
            num_samples = params[3]
            # Determining the sampling rate
            sample_rate = params[2]
            # Determine the number of seconds in the audio file
            duration = num_samples / float(sample_rate)
            # Trim the audio file to 5 seconds if it is longer
            if duration > 5:
                num_samples = 5 * sample_rate
                # Creating a new audio file with cropped data
                with wave.open(os.path.join(output_folder, 'trimmed_' + filename), 'w') as output_file:
                    # Copy the title
                    output_file.setparams(params)
                    # Copy the data
                    data = file.readframes(num_samples)
                    output_file.writeframes(data)
