from openai import OpenAI

api_key = ''
client = OpenAI(api_key=api_key)

instructions = """
당신은 코딩을 재밌게 가르치는 친근한 선생님 역할을 합니다.

## 작업 지침
- 사용자가 이해하기 쉽게, 어려운 용어는 쉬운 말로 풀고, 코딩 개념을 흥미롭

## 컨텍스트
- 입력이 특정 분야와 관련이 있으면, 관련 지식을 반영하세요
- 낯선 단어는 쉬운 말로 바꾸세요.
- 사용자가 초보자일 경우, 단순하고 친근하게 설명하세요.

##  페르소나
- 역할 : 코딩 멘토이자 친근한 선생님
- 톤 : 전문가지만 쉽게 설명
- 어조 : 친근하고 재밌게

사용자가 질문하면, 위 지침을 모두 반영하여 재밌고 이해하기 쉽게 답변해
"""
if "messages" not in st.session_state:
    st.session_state("messages"] = [
        {"role": "system", "content": instructions}
    ]

st.title("나만의 GPT 챗봇")

user_input = st.text_input("질문을 입력하세요:", "")

if user_input
    # 사용자 메시지 추가
    st.session_state["messages"].append({"role": "user", "content": user_input})

    # GPT 호출
    response = client.responses.create(
        model="gpt-4o-mini",
        input=st.session_state["messages"]
    )

    bot_reply = response.output_text

    # 대화 기록 업데이트
    st.session_state["messages"].append({"role": "assistant", "content": bot_reply})

# 대화 내역 출력
for msg in st.session_state["messages"]:
    if msg["role"] != "system":
        st.write(f"**{msg["role"]}**: {msg['content']}")