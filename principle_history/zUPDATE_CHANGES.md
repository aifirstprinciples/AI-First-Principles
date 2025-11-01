# UPDATE_CHANGES - Principle History Management

This document explains how to update the principle history when changes are made to `ai first principles.md`.

## Overview

When `ai first principles.md` is updated, this process maintains a complete history of each principle's evolution in individual markdown files within the `principle_history` directory.

## Process

### Step 1: Read the Current Source File

Read the file `ai first principles.md` from the repository root. Parse it to identify:
- Each principle's title (text in bold, e.g., **Principle Title**)
- Each principle's full content (title + description + italicized guideline)

### Step 2: Compare with Existing History

Check the `principle_history` directory for existing `.md` files (excluding `zUPDATE_CHANGES.md`, `zCHANGELOG.md`, and files in `zArchive/`).

For each existing principle file:
- Read the file to identify the current principle title (from the most recent entry at the top)
- Compare with the principle titles from the source file

### Step 3: Handle Each Principle

For each principle found in `ai first principles.md`:

#### NEW PRINCIPLE
If no existing file matches this principle:
1. Create a new `.md` file named exactly after the principle title (sanitize filename: replace spaces with underscores or hyphens, remove special characters that aren't filesystem-safe)
2. Add the current date (YYYY-MM-DD format)
3. Add a blank line
4. Add the complete principle content (title, description, and guideline)

**Example filename format:** `AI_Inherits_Human_Patterns.md` or `AI-Inherits-Human-Patterns.md`

#### CHANGED PRINCIPLE
If an existing file matches (same or similar title):
1. **Compare content carefully** - if the principle text has changed:
   - Prepend the current date (YYYY-MM-DD format) to the top of the file
   - Add a blank line after the date
   - Add the updated complete principle content
   - History should be newest at the top (reverse chronological)
2. **If the title has changed**:
   - Check if this is truly a title change or a new principle
   - **Default assumption: If the core concept is similar, treat as a changed principle**
   - Rename the existing `.md` file to match the new title (sanitize the filename)
   - Update the file content as described above
3. **If only minor wording changes**: Still add a new dated entry at the top

**Judgment Guidelines:**
- Default to assuming a **change** rather than a new principle when uncertain
- Consider the principle's core message, not just the exact wording
- If the fundamental concept is the same but expressed differently, it's a change
- Only create a new principle if the concept is fundamentally different

#### DELETED PRINCIPLE
If a principle exists in the history files but is NOT found in `ai first principles.md`:
1. Move the principle's `.md` file to `principle_history/zArchive/`
2. Preserve the filename and content exactly as-is (do not add deletion date or modify content)

### Step 4: Date Format

Always use ISO 8601 date format: `YYYY-MM-DD` (e.g., `2025-01-15`)

### Step 5: File Format Standard

Each principle file should follow this structure (newest first):

```markdown
2025-01-15

**Current Principle Title**
Current principle description text with guideline. <u>*Guideline text.*</u>

---

2025-01-10

**Previous Principle Title**
Previous principle description text with guideline. <u>*Previous guideline text.*</u>
```

Note: Use `---` or similar separators between historical entries if needed for readability.

## Key Rules

1. **Default to Change, Not New**: When uncertain if a principle is new or changed, default to treating it as a changed principle
2. **Preserve All History**: Never delete historical entries from principle files
3. **Chronological Order**: Newest entries always at the top
4. **Title Changes**: Update filenames when titles change, but link the history by recognizing the underlying principle
5. **Complete Content**: Each entry should include the full principle (title + description + guideline)

## Example Workflow

1. Read `ai first principles.md`
2. Identify 12 principles (or current count)
3. Check `principle_history/` for existing files
4. For each principle:
   - Match with existing file? → Update existing file
   - No match? → Create new file
   - Existing file not in source? → Move to zArchive
5. Update filenames if titles changed
6. Ensure all dates are current and accurate

## Step 6: Update the Changelog

After making any changes to principles:
1. Open `zCHANGELOG.md` in the `principle_history` directory
2. Add a new entry at the TOP of the file (reverse chronological order)
3. Use the current date in YYYY-MM-DD format
4. Clearly describe what changed:
   - **New Principle**: "Added [Principle Name]"
   - **Updated Principle**: "Updated [Principle Name] - [brief description of what changed]"
   - **Renamed Principle**: "Renamed [Old Name] to [New Name]"
   - **Archived Principle**: "Archived [Principle Name]"
5. Keep entries concise but informative

**Example changelog entry:**
```markdown
### 2025-10-24

- Updated **AI Fails Faster Than Humans React** - Refined language around ambiguous authority and catastrophic delegation
- Added **AI Inherits Human Patterns** - New principle about variation and constraints
- Updated **Ambiguity Is Wisdom** - Minor punctuation change in guideline
```

## Notes

- Always use best judgment when determining if a principle is new or changed
- When in doubt, preserve history by treating as a change
- The goal is to maintain a complete audit trail of how each principle evolves over time
- **ALWAYS update the zCHANGELOG.md file after making any changes to principles**


