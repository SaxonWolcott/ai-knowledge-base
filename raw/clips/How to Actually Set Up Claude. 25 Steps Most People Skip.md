---
title: "How to Actually Set Up Claude. 25 Steps Most People Skip"
source: "https://x.com/eng_khairallah1/status/2059564299555918064"
author:
  - "[[@eng_khairallah1]]"
published: 2026-05-27
created: 2026-06-01
description: "Here is what happens every single day.Save this :)Someone signs up for Claude. They open the chat. They type a question. They get an answer...."
tags:
  - "clippings"
---
![Image](https://pbs.twimg.com/media/HJSFd7ZWwAEotji?format=jpg&name=large)

Here is what happens every single day.

Save this :)

Someone signs up for Claude. They open the chat. They type a question. They get an answer. They think: "okay, this is useful."

Then they keep using it the exact same way for months. One question at a time. No context. No memory. No system. No connected tools. Starting from scratch every single session.

They are using maybe 10% of what Claude can do.

**And the worst part is they do not even know they are leaving 90% on the table.**

I am going to walk you through 25 setup steps that most people never complete. Each one unlocks a layer of capability that transforms Claude from a chatbot you ask questions to into a system that actually works for you.

These are in order. Do them sequentially. Each step builds on the one before it.

**By step 25 you will be using a completely different tool than the one you started with.**

## Steps 1–5: The Foundation Most People Skip

**Step 1: Write Your Custom Instructions**

Go to Settings. Find Custom Instructions. Write at minimum:

Who you are. What you do. Who your audience is. How you prefer Claude to communicate (concise, detailed, casual, formal). What your default output format is.

Two minutes. Transforms every single conversation from that point forward.

Most people leave this blank. They get generic responses. They blame Claude.

**Step 2: Set Your Communication Style Preferences**

In the same settings area, define how Claude talks to you. Do you want short, direct answers? Do you want detailed explanations? Do you want Claude to ask clarifying questions or just make its best attempt?

These preferences apply to every conversation. Set them once and Claude adapts permanently.

**Step 3: Create Your First Project**

Projects are dedicated workspaces with their own system prompts and knowledge files. Do not skip this. Create a project for your primary workflow, whatever you use Claude for most.

Name it clearly. "Content Production." "Business Analysis." "Coding Projects." "Research."

**Step 4: Write Your Project System Prompt**

Inside your project, write a system prompt that defines Claude's role within that workspace. This is more specific than your custom instructions. This tells Claude exactly what it does when you are in this particular project.

Example:

You are my content strategist and writer. Your job in this project is to help me research, plan, write, and edit articles for my audience of \[AUDIENCE\]. My content style: direct, punchy, zero fluff. Short paragraphs. Bold key claims. Specific numbers over vague statements. When I ask you to write, produce a complete draft - not an outline unless I specifically ask for one. When I ask you to edit, be ruthless. Cut anything that does not add value.

**Step 5: Upload Your First Knowledge Files**

Upload at least three reference documents to your project:

1. Your style guide or writing samples (so Claude matches your voice)
2. Your audience profile or customer personas (so Claude knows who it is writing for)
3. Your most important reference document for this workflow (product docs, brand guidelines, strategic plan)

**These five steps take about 15 minutes total. They are the foundation everything else is built on. Most users never complete a single one of them.**

## Steps 6–10: Building Memory and Consistency

**Step 6: Actively Build Memory**

During your next five conversations, explicitly tell Claude to remember important things:

"Remember that I prefer TypeScript over JavaScript." "Remember that my newsletter goes out Tuesdays." "Remember that I never use the word 'leverage' in my content."

Memory compounds. After a month of active building, Claude knows your preferences without being reminded.

**Step 7: Create a Context File**

Create a markdown file called [context.md](http://context.md/) that contains everything Claude needs to know about your current work situation:

- Active projects and their status
- Current priorities for this quarter
- Decisions you have already made (so Claude does not re-debate them)
- Tools and platforms you use
- People you work with and their roles

Upload this to your project. Update it monthly.

**Step 8: Save Your Best Prompts**

Every time a prompt produces an excellent result, save it. Create a /Prompts folder. Store each winning prompt as its own file with a descriptive name: [research-brief-prompt.md](http://research-brief-prompt.md/), [article-first-draft-prompt.md](http://article-first-draft-prompt.md/), [competitor-analysis-prompt.md](http://competitor-analysis-prompt.md/).

Never start from scratch when you have a proven prompt available.

**Step 9: Create Output Templates**

For every deliverable you produce regularly, create a template that defines the exact structure, sections, length, and format. Upload these to your project.

When you need a weekly report: "Use my weekly-report-template and fill it with this week's data."

Templates guarantee consistency. They eliminate the randomness that comes from different prompts producing different structures.

**Step 10: Establish a Quality Checklist**

Write a checklist that defines your quality standards. Add it to your project's system prompt as a final verification step:

"Before delivering any output, verify: all claims include specific numbers, every section has a clear purpose, the opening hook creates genuine curiosity, the tone matches my style guide, and the format follows my template."

Claude runs this check before presenting any output. Quality goes up immediately.

## Steps 11–15: Connecting Claude to Your World

**Step 11: Connect Gmail**

Claude's Gmail connector lets it read your email, draft responses, and search your inbox. The setup takes under two minutes through Claude Desktop.

Once connected, you can say "summarize my important emails from today" and get a prioritized briefing without opening your inbox.

**Step 12: Connect Google Calendar**

Claude reads your schedule, identifies conflicts, and helps you plan your time. "What does my week look like?" becomes a question Claude can answer with actual data instead of asking you to copy-paste your calendar.

**Step 13: Connect Google Drive**

Your documents, spreadsheets, and presentations become accessible to Claude directly. No more downloading files, uploading them to chat, and hoping the formatting survives. Claude reads them where they live.

**Step 14: Connect Slack (If You Use It)**

Claude reads your Slack channels, summarizes conversations, and drafts messages. Combined with a daily scheduled task, this eliminates the need to scroll through channels catching up on everything you missed.

**Step 15: Install Your First MCP Server**

MCP servers give Claude access to external tools and data. Start with Tavily for web search - it gives Claude real-time internet access.

Install it. Connect it. Now when Claude answers a question, it can verify against current information instead of relying on training data that might be outdated.

## Steps 16–20: Installing Claude Desktop and Cowork

**Step 16: Download Claude Desktop**

If you are still using Claude only in the browser, you are missing the most powerful features. Download Claude Desktop from [claude.com/download](http://claude.com/download). Install it. Open it.

You now have access to Chat, Code, and Cowork in one application.

**Step 17: Set Up Cowork Folder Access**

In Claude Desktop, open the Cowork tab. Grant access to the folders where you want Claude to work. Start with your Documents folder and any project-specific folders.

Cowork can now read, create, edit, organize, rename, and move files in those folders. This is where Claude stops being a chatbot and starts being an assistant that touches your actual work.

**Step 18: Run Your First Cowork Task**

Start simple. "Organize my Downloads folder. Put documents in /Docs, images in /Images, delete anything older than 90 days."

Watch Claude actually execute this on your computer. Files moving. Folders being created. Work getting done.

This is the moment most people realize they have been using 10% of the tool.

**Step 19: Set Up Your First Scheduled Task**

Type /schedule in Cowork. Set up one recurring task. Start with something small:

"Every Monday at 8am, check my calendar for the week and save a summary to /Weekly/planning-\[date\].md."

You now have an AI assistant running on autopilot. Most users do not know this feature exists.

**Step 20: Install Your First Plugin**

Go to the Plugin marketplace. Find a plugin that matches your profession or primary workflow. Install it. Learn its slash commands.

Plugins give Claude pre-built specialized workflows. Instead of prompting from scratch, you trigger a complete workflow with one command.

## Steps 21–25: Building the System That Runs Itself

**Step 21: Create Your First Skill**

A Skill is a permanent instruction file that teaches Claude how to execute a specific task. Create one for your most repetitive workflow.

Use Claude to help you build it:

"I do \[THIS TASK\] every week. It involves \[THESE STEPS\]. Turn this into a Claude Skill with clear process steps, output format, and quality standards."

Save the Skill file. Now Claude executes this workflow consistently every single time.

**Step 22: Build Your Morning Automation**

Combine everything you have set up into a single morning briefing:

"Check my email for anything urgent. Summarize overnight Slack messages. Pull my calendar for today. Scan trending topics in my niche. Save a daily briefing to /Daily."

Schedule this at 7am. You wake up to a complete situation report every morning. Total daily time saved: 30 to 45 minutes.

**Step 23: Set Up Your Content Pipeline**

If you create any kind of content, build a multi-step pipeline:

Step 1: Research agent scans for trending topics and saves a brief. Step 2: Outline agent creates three article outlines based on the brief. Step 3: You pick the best outline. Step 4: Writer agent produces the full draft. Step 5: Editor agent polishes to publication quality.

You go from raw topic to finished article with minimal manual effort.

**Step 24: Implement Weekly Refinement**

Every Friday, spend fifteen minutes reviewing Claude's outputs from the week:

What did not meet your standard? What prompt change would fix it? What new workflow could you add?

Update your Skills, templates, and system prompts based on your answers. This weekly habit is the compound effect that separates casual users from power users.

**Step 25: Document Your Entire System**

Create a master file called [my-claude-system.md](http://my-claude-system.md/) that documents everything you have built:

- Your custom instructions
- Your Projects and what each one does
- Your Knowledge files and where they are
- Your connected tools and MCP servers
- Your Skills and workflows
- Your scheduled tasks
- Your templates and prompt library

This file is your operations manual. If you ever need to rebuild your setup, replicate it for a team member, or explain your system to someone else, it is all documented.

## What Your Claude Looks Like After Step 25

Before these steps, Claude is a chatbot. You type a question. You get an answer. You start over next time.

After these steps, Claude is a system. It knows who you are. It remembers your preferences. It accesses your email, calendar, and files. It runs tasks on schedule while you sleep. It produces consistent, high-quality output that matches your standards every time. It gets better every single week because you are refining it constantly.

**Same tool. Same subscription. Completely different experience.**

The difference is not the model. The difference is the setup.

And the setup is exactly what 99% of users never complete.

You just read the complete blueprint. Every step. In order. With exact instructions.

Most people will read all 25 steps and implement zero of them.

The ones who open their settings right now and start with Step 1 will be running a completely different version of Claude by the end of the month. And they will never go back to the old way.

**Follow me** [@eng\_khairallah1](https://x.com/@eng_khairallah1) **for more tools, workflows, and systems. No fluff. Just what works.**

**hope this was useful for you, Khairallah** **❤️**