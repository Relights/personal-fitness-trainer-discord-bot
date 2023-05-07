import discord
import asyncio
import requests
from discord.commands import Option
from random import randint
import string
from telnetlib import theNULL
import nextcord
import asyncio
from nextcord import Interaction
bot = discord.Bot()
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

response = ""
prompt_to_train = "The following is a workout plan for the user based on the following data\nAge:18\nWeight: 170lbs\nHeight:180cm\nGoal: grow muscle\n\nDay 1: Chest and Triceps\n\nBarbell bench press - 4 sets x 8-10 reps\nDumbbell flyes - 3 sets x 12 reps\nIncline dumbbell press - 4 sets x 8-10 reps\nTricep dips - 3 sets x 12 reps\nTricep pushdowns - 3 sets x 12 reps\nDay 2: Back and Biceps\n\nDeadlifts - 4 sets x 8-10 reps\nWide-grip pull-ups - 3 sets x max reps\nSeated cable rows - 4 sets x 8-10 reps\nBarbell curls - 3 sets x 12 reps\nHammer curls - 3 sets x 12 reps\nDay 3: Rest\n\nDay 4: Legs and Shoulders\n\nBarbell squats - 4 sets x 8-10 reps\nLeg press - 3 sets x 12 reps\nRomanian deadlifts - 4 sets x 8-10 reps\nSeated dumbbell shoulder press - 4 sets x 8-10 reps\nLateral raises - 3 sets x 12 reps\nFront raises - 3 sets x 12 reps\nDay 5: Arms and Abs\n\nSkullcrushers - 3 sets x 12 reps\nCable curls - 3 sets x 12 reps\nOverhead tricep extensions - 3 sets x 12 reps\nPreacher curls - 3 sets x 12 reps\nPlank - 3 sets x 60 seconds\nRussian twists - 3 sets x 20 reps\nFor each exercise, choose a weight that allows you to complete the prescribed number of reps with proper form. Rest 60-90 seconds between sets, and make sure to warm up before each workout with some light cardio and stretching. Remember to also incorporate proper nutrition, including enough protein and calories, to support muscle growth.\n\n##########################\nThe following is a workout plan for the user based on the following data\nAge:90\nHeight:160lbs\nHeight:175cm\nGoal: live longer\n\nDay 1: Cardio\n\nBrisk walking or light cycling - 30 minutes\nDay 2: Strength and Balance\n\nBodyweight squats - 2 sets x 10 reps\nWall push-ups - 2 sets x 10 reps\nSeated leg extensions - 2 sets x 10 reps\nSeated dumbbell shoulder press - 2 sets x 10 reps\nStanding heel raises - 2 sets x 10 reps\nOne-legged balance - 3 sets x 30 seconds each leg\nDay 3: Cardio\n\nBrisk walking or light cycling - 30 minutes\nDay 4: Flexibility and Balance\n\nSeated hamstring stretch - 2 sets x 30 seconds each leg\nSeated butterfly stretch - 2 sets x 30 seconds\nSeated spinal twist - 2 sets x 30 seconds each side\nOne-legged balance with eyes closed - 3 sets x 30 seconds each leg\nDay 5: Strength and Cardio\n\nBrisk walking or light cycling - 10 minutes\nChair squats - 2 sets x 10 reps\nWall push-ups - 2 sets x 10 reps\nSeated row - 2 sets x 10 reps\nSeated dumbbell curls - 2 sets x 10 reps\nIt's important to remember that any exercise program should be tailored to an individual's specific needs, so if there are any physical limitations or health concerns, it's best to consult with a doctor or a qualified personal trainer before starting any exercise program. Additionally, it's important to stay properly hydrated and to listen to your body and take breaks as needed.\n\n##########################\nThe following is a workout plan for the user based on the following data\nAge:18\nHeight:300lbs\nHeight:185cm\nGoal: lose weight\n\nDay 1: Cardio\n\nTreadmill walking - 30 minutes at a brisk pace (3.5-4 mph) with incline set at 1-2%\nDay 2: Strength and Cardio\n\nBodyweight squats - 3 sets x 15 reps\nPush-ups - 3 sets x 10 reps\nLunges - 3 sets x 10 reps each leg\nDumbbell rows - 3 sets x 10 reps each arm\nTreadmill walking or jogging - 20 minutes at a moderate pace (4-5 mph)\nDay 3: Rest\n\nDay 4: Cardio\n\nElliptical machine - 30 minutes at a moderate pace with resistance set to a comfortable level\nDay 5: Strength and Cardio\n\nDumbbell bench press - 3 sets x 10 reps\nDumbbell curls - 3 sets x 10 reps\nTricep extensions - 3 sets x 10 reps\nSeated dumbbell shoulder press - 3 sets x 10 reps\nTreadmill walking or jogging - 20 minutes at a moderate pace (4-5 mph)\nDay 6: Cardio\n\nStationary bike - 30 minutes at a moderate pace with resistance set to a comfortable level\nIt's important to remember that weight loss also depends on diet, so it's important to also focus on proper nutrition to support weight loss goals. Additionally, it's important to listen to your body and take breaks as needed. If there are any physical limitations or health concerns, it's best to consult with a doctor or a qualified personal trainer before starting any exercise program.\n\n##########################\nThe following is a workout plan for the user based on the following data\nAge:40\nHeight:200lbs\nHeight:180cm\nGoal: cardiovascular endurance\nDay 1: Strength\n\nBarbell squats - 3 sets x 10 reps\nDeadlifts - 3 sets x 10 reps\nBench press - 3 sets x 10 reps\nStanding military press - 3 sets x 10 reps\nBent-over barbell rows - 3 sets x 10 reps\nDay 2: Cardio\n\nRunning or jogging - 30 minutes at a moderate pace (5-6 mph)\nDay 3: Strength and Endurance\n\nDumbbell lunges - 3 sets x 10 reps each leg\nDumbbell step-ups - 3 sets x 10 reps each leg\nDumbbell bicep curls - 3 sets x 10 reps\nDumbbell tricep extensions - 3 sets x 10 reps\nPlanks - 3 sets x 30 seconds\nDay 4: Rest\n\nDay 5: Strength and Cardio\n\nIncline dumbbell bench press - 3 sets x 10 reps\nStanding dumbbell curls - 3 sets x 10 reps\nSkull crushers - 3 sets x 10 reps\nSeated dumbbell shoulder press - 3 sets x 10 reps\nStationary bike - 30 minutes at a moderate pace with resistance set to a comfortable level\nDay 6: Endurance\n\nSwimming - 30 minutes at a moderate pace\nIt's important to remember that weight gain also depends on diet, so it's important to focus on proper nutrition to support weight gain goals. Additionally, it's important to listen to your body and take breaks as needed. If there are any physical limitations or health concerns, it's best to consult with a doctor or a qualified personal trainer before starting any exercise program.\n\n##########################\n"
def generate_response(txt):
    url = "https://api.ai21.com/studio/v1/j2-jumbo-instruct/complete"

    payload = {
        "numResults": 1,
        "maxTokens": 500,
        "minTokens": 100,
        "temperature": 0.75,
        "topP": 0.9,
        "topKReturn": 0,
        "stopSequences": ["##########################","##########################\n","#"],
        "frequencyPenalty": {
            "scale": 0,
            "applyToWhitespaces": True,
            "applyToPunctuations": True,
            "applyToNumbers": True,
            "applyToStopwords": True,
            "applyToEmojis": True
        },
        "presencePenalty": {
            "scale": 0,
            "applyToWhitespaces": True,
            "applyToPunctuations": True,
            "applyToNumbers": True,
            "applyToStopwords": True,
            "applyToEmojis": True
        },
        "countPenalty": {
            "scale": 0,
            "applyToWhitespaces": True,
            "applyToPunctuations": True,
            "applyToNumbers": True,
            "applyToStopwords": True,
            "applyToEmojis": True
        },
        "prompt": txt
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "Bearer API_KEY"
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.json()['completions'][0]['data']['text']



@bot.slash_command(name="workout_planner", guild_ids=guild_ids])
async def workout_planner(ctx, age: Option(str, "Age", required = True, default = '18'), weight: Option(str, "Weight (In lbs)", 
                          required = True, default = ''), height: Option(str, "Height (in cm)", required = True, default = ''), goal: Option(str, "Goal", required = True, default = "Hypertrophy")):
                                    global prompt_to_train
                                    global response
                                    prompt = "The following is a workout plan for the user based on the following data\nAge:"+age+"\nWeight: "+weight+"lbs"+"\nHeight: "+height+"cm"+"\nGoal:"+goal+"\n\nWorkout plan:\n"
                                    prompt_to_train += prompt
                                    response = ""
                                    await ctx.defer()
                                    response = generate_response(prompt_to_train)
                                    prompt_to_train += response+"##########################\n"      
                                    embed=discord.Embed(title="Workout plan", description="The following is a workout plan for the user based on the following data\nAge:"+age+"\nWeight: "+weight+"lbs"+"\nHeight: "+height+"cm"+"\nGoal:"+goal+"\n\nWorkout plan:\n\n"+response, color=discord.Color.dark_teal())
                                    embed.set_author(name=ctx.author.name)

                                    await ctx.respond(embed = embed)
                                    print(prompt_to_train)

bot.run('token')
