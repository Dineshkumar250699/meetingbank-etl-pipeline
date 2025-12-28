import json
from pathlib import Path

# Check the CLEANED data (before transformation)
cleaned_file = list(Path('data/cleaned').glob('meetings_cleaned_*.json'))[0]
print(f"Checking: {cleaned_file}\n")

with open(cleaned_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

meetings = data.get('meetings', [])
print(f"Total meetings: {len(meetings)}\n")

# Check first 5 for agendas
for i, meeting in enumerate(meetings[:5]):
    meeting_id = meeting.get('meeting_id', 'unknown')
    agenda = meeting.get('agenda', [])
    print(f"{i+1}. Meeting {meeting_id}:")
    print(f"   Agenda items: {len(agenda)}")
    if agenda:
        print(f"   First item: {agenda[0]}")
    print()

# Total agendas
total = sum(len(m.get('agenda', [])) for m in meetings)
print(f"TOTAL AGENDA ITEMS: {total}")