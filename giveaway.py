import instaloader
import random

print("""\033[1m\033[93m
     _   _ _ _       _       _   _ _      _
    | | | (_) |_ ___| |__   | | | (_) ___| | _____ _ __
    \033[1m\033[92m| |_| | | __/ __| '_ \  | |_| | |/ __| |/ / _ \ '__|
    |  _  | | || (__| | | | |  _  | | (__|   <  __/ |
    \033[1m\033[94m|_| |_|_|\__\___|_| |_| |_| |_|_|\___|_|\_\___|_|   """)

print("""
  \033[42m\033[1;30m===================Instagram Giveaway===================\033[0;m
\033[0;m""")

a = input("   \33[104mPlease enter insta post link :\033[1;0m ")

pcode = a.split('/')[-2]

L = instaloader.Instaloader()

post =  instaloader.Post.from_shortcode(L.context,pcode) #paste post code here

post_comments = post.get_comments()

users_list = []

for comment in post_comments:
    user = str(comment.owner.username)
    users_list.append(user)

i = random.randint(0,len(users_list)-1)

# print(f"total users : {len(users_list)}")

print(f"\n   \033[1m\033[95m Total Users :\033[1;0m {len(users_list)}")

print(f"\n   \033[1m\033[95m Winner is :\033[1;0m {users_list[i]}")

print(f"\n     \033[42m\033[1;30mCongratulations {users_list[i]} :)\033[1;0m")