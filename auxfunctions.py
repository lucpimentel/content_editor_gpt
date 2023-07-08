from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate


sys_msg_template = '''You are Draft Corrector GPT.
I will give you one of my draft paragraphs and you will correct it for me.

Please abide to the following rules:
- Keep your language simple and clear.
- Write in direct form.
- Prefer to use nouns and verbs.
- Prefer to use short words.
- Keep the same structure of the draft.
- Keep the same points of the draft.
- Prefer to use vivid words.

Begin!'''




sys_msg_prompt = SystemMessagePromptTemplate.from_template(sys_msg_template)

human_msg_template = '{input}'
human_msg_prompt = HumanMessagePromptTemplate.from_template(human_msg_template)

chat_prompt = ChatPromptTemplate.from_messages([sys_msg_prompt,human_msg_prompt])
