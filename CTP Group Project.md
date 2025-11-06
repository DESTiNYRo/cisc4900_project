# Group Project

# CTP Group Project

# Members and Roles

* **Destiny Rosado Salcedo** \- Frontend  
* **Faizan Khan** \- Slackbot/Discordbot  
* **Jessica Chen** \- Backend  
* **Oleksii Sudarin** \- Cluster Graph  
* **Eric Azayez** \- TBD

# Brainstorm/Ideas

| Project | Description |
| :---: | ----- |
| Health (Destiny) | An application on our mobile device that will do a gait analysis and inform user of potential mobility issues  Can develop on android to start off |
| Education (Destiny/Faizan) | Personal study buddy Observe users study habits(time spent on a topic/subject, how many breaks taken) and propose better study habits to maximize their learning capabilities |
| Baking (Jessica) | An application where the user will input ingredients and the program will output substitutes the user can use to replace the ingredient.  |
| Slack/Discord Finder and Stats App (Oleksii) | A cluster graph visual search app for finding topic related messages for easier search for needed information. Have extra information that showcases activity of a desired person or activity of a channel. |

**Features:**  
**Project Name**  
Slack Cluster Finder  
**Project Scope (Objective)**  
**Audience (Who is this project for?)**

- Anyone who uses Slack or Discord and takes parts in servers  
- For big servers where there are too many materials for someone to sift through

**Key Features**

- Queries  
- Filters  
- Dynamic Cluster Graph Visualization

**Frameworks/Libraries (Tech Stack)**

- SlackBot (TypeScript)  
- Python (Plotly)  
- Backend (Flask, FastAPI)  
- Frontend (React)  
- DiscordBot (Python/JavaScript)

**List of Tasks**  
**Divide/Assign Tasks Per Person**  
Frontend \- Setup frontend folder with React \+ Vite  
Backend \- Setup backend folder with store and catch the data  
Visualization Graph \- Create a cluster graph using sample data  
SlackBot \- Create the basic SlackBot  
DiscordBot Create the basic DiscordBot

**Timeline Of Project**  
**Implementation Plan**

- Website to visualize the data  
- Slack and Discord bots (main objective is Slack)

**Datasets To Be Used (With Their Links)**

- **Hugging Face: all-MiniLM-L6-v2**

Fast LLM for sentence embeddings 

**Video Tutorials Related To Your Project (With Their Links)**  
**Workflow Diagram (use any software you like to generate one)**

- Figma

**Example Cluster for a dataset**  
Latent-scope: [https://github.com/enjalot/latent-scope?tab=readme-ov-file](https://github.com/enjalot/latent-scope?tab=readme-ov-file)  
How it works (very general):  
Data \-\> goes through embedder \-\> UMAP for the cluster \-\> cluster map\!

Example:   
Input: One group chat  
Output: Clusters chat into topics

Bots use?  
Set up for basics, will build on later

How is the data going to be structured?  
database for authentication with discord/slack and storing data

Faizan:

- Change the bots \- Slack create a mock workspace to test it out, Discord make a mock server to test it out  
- Extract all the data (i.e. messages for Slack and Discord)  
- Find out how to store the data. 

# Eric

[User Stories](https://docs.google.com/presentation/d/161W3rAAaOnCAXY_PIXDuZoORVtzSOWgVxvu-r6n7ktY/edit?slide=id.g39e5ebc02c5_0_8#slide=id.g39e5ebc02c5_0_8)

[User Flow Ideas](https://excalidraw.com/#room=bb77add24a0020a821f8,e2DVn3gK3NPjGy16ezCYCA)

[Github Link](https://github.com/oleksiisud/slack-cluster-finder/tree/main)

Backend Saves Authentication Details

* UI Idea: Ctrl F show the search icon. We can find a similar hotkey (CTRL G) for Context Search  
  * Littlebit

Demo Idea / Proof of Concept: Have users search for a prompt manually, then with context search  
Name:   
 

Useful Resources  
---

Message Tagging [Convo 7 Years Ago](https://stats.stackexchange.com/questions/369545/clustering-short-messages)

Notes on Clustering

---

[https://www.mdpi.com/2076-3417/13/1/342](https://www.mdpi.com/2076-3417/13/1/342)  
Tokenization is defined as a standard text representation that divides a flow of natural language text into distinct significant elements called tokens as part of the pre-processing

Whilst clustering search results, noise filtering is an essential task of the tokenizer.

Hierarchical Clustering  
Parent and child clusters. For example  
A: is tree, is plant, is alive  
B: is plant, is alive

Partitional Clustering  
Items are fully independent  
K-Means clustering

Fuzzy, or Soft Clustering  
Items overlap 

RAAG, Fine Tuning, 

# Project Walkthrough

Bots \-\> extract data   
Bots use?  
Set up for basics, will build on later

How is the data going to be structured?  
database for authentication with discord/slack and storing data

Slack Bots could extract data to cluster for us

Frontend 

- Set up   
- Login/Auth (Login/signup page similar to githubs?)

Database: MongoDB or Supabase

- Slack/Discord Auth

# FeatureList

