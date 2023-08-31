# 1st-Frame-Grabber
Python Script to quickly bulk collect the 1st frame of gifs as .pngs.

As default takes draws from subfolder *gif* and outputs to *png*.

If you wish to prefix your output files
    
    output_path = os.path.join(output_folder, f'INSERT PREFIX HERE {idx}.png')

 Eg: 'Cowhat {idx}.png' for Cowhat 0.png etc
