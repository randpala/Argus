import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

# SECRET
supabase_key = os.environ['SUPABASE']

# Create Supabase Client
supabase = create_client("https://iiajztizubphlsvhbhvq.supabase.co", supabase_key)
# XP incremenet in Supabase
async def xp_increment(amount, id) -> None:
  try:
    xptable = supabase.table('XPTable').select('xp').eq('author', id).execute()
    temp3 = xptable.data[0]['xp']
    supabase.table('XPTable').update({'xp': temp3 + amount}).eq('author', id).execute()
  except Exception as e:
    print(e)
# List of every user in Supabase
LIST_TMP = supabase.table('XPTable').select('author').execute()
LIST_ID = []
for i in LIST_TMP.data:
  LIST_ID.append(i['author'])