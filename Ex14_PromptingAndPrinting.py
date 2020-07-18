from sys import argv
script_name, user_name = argv
prompt ='>'

print(f'hi {user_name}, im script{script_name}')
print('i would like to ask few questions')
print(f'do you like me, {user_name}')
likes = input(prompt)

print('where do you live')
place = input(prompt)

print('which computer do you have')
comp = input(prompt)

print(f"""
So {user_name} you said you {likes} about liking me.
And you live at {place}.
And you have {comp} computer. Cool
""")
