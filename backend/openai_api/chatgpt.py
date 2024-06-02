from openai import OpenAI

from models import Character
from openai_api.event_handler import EventHandler
import os 
import requests
import random
import json

client = OpenAI()

image_dir = "images"

def generate_options(char1: Character, player: Character, goal1: str, goal2: str):
    s = ""
    s += "Characteristics:\n"
    s += str({"name": char1.name, "personality": char1.personality, "goal": goal1 }) + "\n"
    s += str({"name": player.name, "personality": player.personality, "goal": goal2 }) + "\n\n"
    
    s += 'Based on this data, give me dialog in json format between this characters, from 4 to 10 lines. Format {"messages": [{"author": "author", "content": "content"}]}'
    
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "user", "content": s}
      ]
    )
    
    obj = json.loads(completion.choices[0].message.content)
    return obj
    
    
def generate_concept_art(project_name: str, project_desc: str, relation: Character, desc: str) -> str:
    response = client.images.generate(
      model="dall-e-3",
      prompt="Game name: %s.\nGame description: %s.\nCharacter name: %s.\nCharacter appearance: %s.\nCharacter personality: %s.\nConcept art description: %s.\nCreate an concept art of this character for this game.\nDon't add any symbols to the image.\n Do not write anything in the image." % (project_name, project_desc, relation.name, relation.appearance, relation.personality, desc),
      size="1024x1024",
      quality="standard",
      n=1,
    )
    
    generated_image_name = relation.name + str(random.randint(0, 100)) + ".png"
    generated_image_filepath = os.path.join(image_dir, generated_image_name)
    generated_image_url = response.data[0].url
    generated_image = requests.get(generated_image_url).content

    with open(generated_image_filepath, "wb+") as image_file:
        image_file.write(generated_image)
    
    return generated_image_name
  
def generate_project_image(project_name: str, project_desc: str) -> str:
    response = client.images.generate(
      model="dall-e-3",
      prompt="Game name: %s.\nGame description: %s.\nCreate an logotype for this game.\nDon't add any letters to the logo." % (project_name, project_desc),
      size="1024x1024",
      quality="standard",
      n=1,
    )
    
    generated_image_name = project_name + str(random.randint(0, 100)) + ".png"
    generated_image_filepath = os.path.join(image_dir, generated_image_name)
    generated_image_url = response.data[0].url
    generated_image = requests.get(generated_image_url).content

    with open(generated_image_filepath, "wb+") as image_file:
        image_file.write(generated_image)
    
    return generated_image_name
  
def generate_project_name(project_desc: str) -> str:
    promt = "Game description: %s.\nCome up with a name for the game.\nIt should be short. Make it unique. Do not include any special symbols in answer." % (project_desc)
    
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "user", "content": promt}
      ]
    )
    
    return completion.choices[0].message.content
  
def generate_character(project_name: str, project_desc: str, charcs: list[Character]) -> str:
  
    promt = 'Create character for game:\nGame name: %s\nGame description: %s.\nFormat: {"name": "name", "personality": "appearance", "appearance": "appearance"}. No more than 40 words.\n' % (project_name, project_desc)
    promt += 'Existing characters: \n'
    for i in charcs:
      promt += '{ "name": "' + i.name + '", "personality": "' + i.personality + '", "appearance": "' + i.appearance + '"}\n'
      
    promt += "Try to avoid repetitions!\n"
    print(promt)
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "user", "content": promt}
      ]
    )
    
    return completion.choices[0].message.content
  