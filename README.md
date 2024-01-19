# auto_backup_obsidian_notes
This is a small script and cronjob to backup obsidian notes on a set schedule.


# Make script executable:

```
chmod +x /path/to/auto_backup_notes.py
```

# Make script auto-run (MacOS only):

### Edit the Crontab
Open Crontab: Open your crontab file in edit mode by running:

```bash
crontab -e
```

### Add a Cron Job: 
In the crontab file, add a line that specifies when and how often the script should run. The cron tab entry should also include a path to a virtualenv so the script can run with all required dependencies:

```bash
0 */3 * * * /Users/{example_name}/.virtualenvs/backup_notes/bin/activate && /Users/{example_name}projects/backup_notes/auto_backup_obsidian_notes/auto_backup_notes.py
```

Each asterisk corresponds to (in order): minute, hour, day of the month, month, day of the week. You can use numbers or special characters like * (any value) or / (every n minutes/hours/etc.).

For example, to run the script every day at 5 PM, you would add:

```bash
0 17 * * * /path/to/your/auto_backup_notes.py
```

Save and Exit: 
After adding the line, save and exit the editor. This will automatically update your crontab.

### Verify Cron Job
Check Crontab List: To verify your cron jobs, list your current cron jobs with:

```bash
crontab -l
```