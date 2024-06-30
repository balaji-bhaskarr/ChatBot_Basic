from openai import OpenAI
import time

client = OpenAI(api_key='sk-proj-********')


def chat_with_gpt(prompt):
    try:
        request = client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[{'role':'user', 'content':prompt}]
            )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(e)
        time.sleep(30)
        return 'There was exception in receiving response, please try later.'

if __name__=='__main__':
    while True:
        user_input = input('You: ')
        if user_input.lower() in ["exit", "bye", "quit"]:
            print('Thank you for using me, I hope I have helped you with your queries.')
            break
        response = chat_with_gpt(user_input)
        print('Response : ', response)