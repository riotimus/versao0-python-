import os
#relevant_path = 'D:\freelancer\biomecanica'
relevant_path = r'D:\freelancer\biomecanica'
included_extensions = ['jpg','jpeg', 'bmp', 'png', 'gif']
file_names = [fn for fn in os.listdir(relevant_path)
              if any(fn.endswith(ext) for ext in included_extensions)]
