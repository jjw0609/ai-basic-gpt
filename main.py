from openai import OpenAI

api_key = ''
client = OpenAI(api_key=api_key)


res1 = client.responses.create(
    model="gpt-4o-mini",
    input="프랑스의 수도는?",
    store=True
)

print(res1.output_text)

res2 = client.responses.creat(
    model="gpt-4o-mini",
    input="프랑스의 인구는?",
    previous_response_id=res1.id,
    store=True
)

print(res2.output_text)


answer = client.responses.create(
    model="gpt-4o-mini",
    input="지금 프랑스 대통령이 누구야?",
    tools=[{"type": "web_search_preview"}]
)

print(answer.output_text)