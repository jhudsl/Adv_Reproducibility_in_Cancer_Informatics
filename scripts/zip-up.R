#!/usr/bin/env Rscript

# Establish base dir
root_dir <- rprojroot::find_root(rprojroot::has_dir(".git"))

chapter_zip_dir <- file.path(root_dir, "chapter-zips")

# Create chapters directory if it doesn't exist
if (!dir.exists(chapter_zip_dir)){
  dir.create(chapter_zip_dir)
}

# Declare python and R directories
py_dir <- file.path(root_dir, "python-examples")
r_dir <- file.path(root_dir, "r-examples")

# Collect all the chapter directories
chapters <- c(dir(py_dir, full.names = TRUE), 
              dir(r_dir, full.names = TRUE))

# Remove the docker ones
chapters <- grep("docker", chapters, invert = TRUE, value = TRUE)

# Now zip them all up
lapply(chapters, function(chapter_dir) {

  original_wd <- getwd()
  # I have to do a bad thing to get rid of the parent folders and I don't know how to get around this 
  setwd(dirname(chapter_dir))
  
  # Declare zip file name 
  output_file <- file.path(paste0(basename(chapter_dir), ".zip"))
  
  # Do the zipping
  zip(output_file, basename(chapter_dir))

  # Move zip to chapter-zips dir
  fs::file_copy(path = output_file,
                new_path = file.path(chapter_zip_dir, output_file), 
                overwrite = TRUE)
  
  # Remove the original file
  file.remove(output_file)
  
  # Reset to the original working directory 
  setwd(original_wd)
  })
