# Install the docx2txt package
# pip install docx2txt
# Import the library
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import docx2txt
import pdf_to_text
# Load the data
from google.colab import files
uploaded = files.upload()

# Store the resume in a variable
resume = docx2txt.process("python_resume.docx")

# Print the resume
print(resume)

# Store the job description into a variable
job_description = docx2txt.process("job_description.docx")

# Print the job description
print(job_description)

# A list of text
text = [resume, job_description]

cv = CountVectorizer()
count_matrix = cv.fit_transform(text)


# Print the similarity scores
print("\nSimilarity Scores:")
print(cosine_similarity(count_matrix))

# get the match percentage
matchPercentage = cosine_similarity(count_matrix)[0][1] * 100
matchPercentage = round(matchPercentage, 2)  # round to two decimal
print("Your resume matches about " +
      str(matchPercentage) + "% of the job description.")
