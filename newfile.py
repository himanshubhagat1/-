import telethon
import random
import os
from time import sleep
from telethon import TelegramClient,events
from telethon.sessions import StringSession
from telethon.sync import TelegramClient, events
from telethon.tl.custom import Button
import tracemalloc
import requests
import sys
x=telethon.__version__

tracemalloc.start()


api_id=4667047           
api_hash="c40d147789f0e194816dc02d948f88db"
string = '1BVtsOHsBu2p4aL3JG4nM_5fpXO3nrESiFVhTTct7MvFnWNkMsWKmmmZOKOJ8V8a1kYqCZi8JTqpoPlxvcGWz_bQATR5aYa6lJhaNGZoKF9n3L2bcWqc9sJ_E3TH-tBOLVas6z0KGBvCES3cuLNso244Eqzw6g9vILnuFut1pBf3o8iOqr20Hyq7iUWRZRmoztNwmrOshHk8AxLpmrX_fl6pLCHbp1jiEYk5QXvBgzcDqucYXOYbD0XBOysGXdg1KudkP-Yk5Rq9KrlzBwTdKlSCyPEQpD0ZByoXLHhYoXVxc2cdYvgBiIJ3P1TDF1dY8VVZ4ScdhyltUlmsi7jvisQl3-Lll7ew='


with TelegramClient(StringSession(string),api_id, api_hash) as client:
    

   
    
    @client.on(events.NewMessage(pattern=r".hii",outgoing=True))
    async def my_event_handler(event):
             await event.edit('Hey Wassup?')
             
             
@client.on(events.NewMessage(pattern=r".maachuda",outgoing=True))
async def my_event_handler(event):
             await event.edit('**Tu Maa Chuda Madarchod**')
             sleep(1)
             await event.edit('Randi')
             
             
@client.on(events.NewMessage(pattern=r".alive",outgoing=True))             
async def my_event_handler(event):
             await event.edit('𝐌𝐁 𝐊𝐈𝐋𝐋𝐄𝐑 IS WORKING AS FUCK\n \nTelethon Version - **1.24.00**\n                                \nPython Version - **3.0**')
             
             
@client.on(events.NewMessage(pattern=r".ping",outgoing=True))             
async def my_event_handler(event):
             await event.edit('**† ♕ ᑭσɳց! ♕ †**'
              '                       \n \n**`Time Taken -  "Unknown ms"`**')
              
@client.on(events.NewMessage)
async def my_event_handler(event):
                    if '.fuck' in event.raw_text:
                        await event.reply('Ohh Yeah')
                        await event.edit('👉       ✊️') 
                        sleep(1)
                        await event.edit('👉      ✊️')
                        sleep(1)
                        await event.edit('👉    ✊️')
                        sleep(1)
                        await event.edit('👉   ✊️')
                        sleep(1)
                        await event.edit('👉✊️💦')
                        sleep(1)
                        await event.edit('**fUcKED**')
                        sleep(2)
                        await event.delete()
    
    
    
@client.on(events.NewMessage(pattern=r".insult",outgoing=True))
async def my_event_handler(event):
                        n=random.randint(1,10)
                        if n==1:
                            await event.edit('Light travels faster than sound, which is why you seemed bright until you spoke.')
                        elif n==2:
                               await event.edit('Your secrets are always safe with me. I never even listen when you tell me them.')
                        elif n==3:
                             await event.edit('Your face makes onions cry.')
                        elif n==4:
                             await event.edit('Don’t be ashamed of who you are. That’s your parents’ job.')
                        elif n==5:
                           await event.edit('If you’re going to be two-faced, at least make one of them pretty.') 
                        elif n==6:
                           await event.edit('You are like a cloud. When you disappear, it’s a beautiful day.')
                        elif n==7:
                           await event.edit('You just might be why the middle finger was invented in the first place.')
                        elif n==8:
                           await event.edit('Wish I had a flip phone so I could slam it shut on this conversation.')
                        elif n==9:
                         await event.edit('You’re cute. Like my dog. He also always chases his tail for entertainment.')
                        elif n==10:
                             await event.edit('Child, I’ve forgotten more than you ever knew.')
                        elif n==11:
                             await event.edit('Light travels faster than sound, which is why you seemed bright until you spoke.')
                             
                             
                             
@client.on(events.NewMessage(pattern=r".sgali",outgoing=True))
async def my_event_handler(event):
                   # if '.sgali' in event.raw_text:
                        await event.reply('**MARDARCHOD KA BETA**')
                        sleep(.5)
                        await event.reply('**TERA MAA KO TOH SABSE PHELE BAR MAINE HI CHODA THA JAPANI TEL LAGA KE**')
                        sleep(.5)
                        await event.reply('**MADHAR CHOD RANDI KA AULAD SALA**')
                        sleep(.5)
                        await event.reply('**TERI BEHNO KO BHI MAINE CHODA THA UNKE SHASDI KI RAAT KO**')
                        
                        
                        
                        
                        
                          
@client.on(events.NewMessage(pattern=r".nice",outgoing=True))
async def my_event_handler(event):
     await event.edit('👏👏**NOICE!**')



@client.on(events.NewMessage(pattern=r".ok",outgoing=True))
async def my_event_handler(event):
    await event.edit('**OKY BABES**')                      
                        
                        
                        

                       
                                              
                                                                                            
                         
"""@client.on(events.NewMessage(pattern=r"",incoming=True))
async def my_event_handler(event):
    await event.reply('Hello, This is 𝐌𝐁 𝐊𝐈𝐋𝐋𝐄𝐑 UserBot                                                                    \nThis is my master Legend\'s Inbox                  **\nPLEASE DO NOT SPAM MY DM, I WILL REPLY YOU AFTER COME BACK ONLINE!**')"""
     
      
             

client.start()
client.run_until_disconnected()
    