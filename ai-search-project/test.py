from google import genai

client = genai.Client(api_key="AIzaSyCKJT_zqITRjj_MHMDC08QlfbPDnOzouyY")

res = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Hello"
)

print(res.text)