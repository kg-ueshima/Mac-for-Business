# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a personal knowledge management system that combines Zettelkasten methodology with business automation. The project manages IT Solution Manager and General Affairs Manager tasks while organizing knowledge systematically.

## Common Development Commands

### Environment Setup
```bash
# Create and activate Python virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Copy environment variables
cp env.example env.local
# Edit env.local with actual values
```

### Daily Automation Scripts
```bash
# Run schedule synchronization
python3 Agents/schedule_updater/auto_schedule_sync.py

# Generate daily report
python3 Agents/daily_report/main.py
# Generate report for specific date
python3 Agents/daily_report/main.py 2025-07-24

# Run clippings sorter
python3 Agents/clippings_sort/run_enhanced_clippings_sorter.py

# Backup to OneDrive
rsync -avh --delete --exclude '.git' --exclude '.venv' --exclude '.obsidian' '/Users/ueshima/Workspace/Mac for Business/' '/Users/ueshima/Library/CloudStorage/OneDrive-医療法人社団　慶友会　吉田病院/Mac for Business-backup'
```

## Architecture Overview

### Knowledge Management Structure (Zettelkasten)
- **01-Fleeting-Notes/**: Temporary notes and quick ideas
- **02-Literature-Notes/**: Processed external information with sources
- **03-Permanent-Notes/**: Conceptualized knowledge with cross-references
- **04-Index-Notes/**: Project-wide indexes and relationships
- **05-Structure-Notes/**: System structure and rules documentation

### Business Folders
- **80-業務日報/**: Daily business reports organized by date
- **80-総務/**: General affairs documents and procedures
- **80-ITソ/**: IT solutions documentation and prompts
- **Clippings/**: Web articles and external content collection

### Automation Agents

#### Daily Report Agent (`Agents/daily_report/`)
Collects information from multiple sources to generate daily reports:
- Teams messages and channel posts
- Sent emails via Microsoft Graph API
- OneDrive new files with Gemini summarization
- Google Calendar events
- Uses Microsoft Graph API with MSAL authentication
- Supports date specification via command line arguments

#### Clippings Sorter Agent (`Agents/clippings_sort/`)
Automatically categorizes and processes Clippings content:
- Tags and sorts Markdown files by content
- Creates permanent notes with merged similar content
- Generates category indexes and structure files
- Uses AI (via Google Gemini) for content analysis
- Limits permanent notes to 15 per category

#### Schedule Updater Agent (`Agents/schedule_updater/`)
Synchronizes schedules between systems:
- Google Calendar integration
- Service account authentication
- Automated schedule updates

## Key Dependencies
- **msal**: Microsoft Authentication Library for Teams/OneDrive/Email
- **requests**: HTTP client for API interactions
- **python-dotenv**: Environment variable management
- **PyYAML**: YAML file processing

## Important Notes
- Environment variables must be set in `env.local` (never commit this file)
- Token files (`token*.json`, `token_cache*.bin`) contain authentication data
- The project uses Microsoft Graph API extensively for automation
- Google Gemini API is used for content summarization
- All scripts expect to run from the project root directory