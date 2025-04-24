<!-- PROJECT LOGO -->
<br />
<p align="center">
  <!-- <a href="https://github.com/agentsea/skillpacks">
    <img src="https://project-logo.png" alt="Logo" width="80">
  </a> -->

  <h1 align="center">Surfkit</h1>

  <p align="center">
    A toolkit for building and sharing AI agents that operate on devices
    <br />
    <a href="https://docs.hub.agentsea.ai/introduction"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://youtu.be/exoOUUwFRB8">View Demo</a>
    ·
    <a href="https://github.com/agentsea/surfkit/issues">Report Bug</a>
    ·
    <a href="https://github.com/agentsea/surfkit/issues">Request Feature</a>
  </p>
  <br>
</p>

## Features

- **Build** multimodal agents that can operate on devices
- **Share** agents with the community
- **Run** agents and devices locally or in the cloud
- **Manage** agent tasks at scale
- **Track** and observe agent actions

## Demo

https://github.com/agentsea/surfkit/assets/5533189/98b7714d-9692-4369-8fbf-88aff61e741c

## Installation

```sh
pip install surfkit
```

## Quickstart

### Prerequisites

- Docker
- Python >= 3.10
- MacOS or Linux

### Python

Use an agent to solve a task

```python
from surfkit import solve

task = solve(
    "Search for the most common variety of french duck",
    agent_type="pbarker/SurfPizza",
    device_type="desktop",
  )

task.wait_for_done()

result = task.result
```

### CLI

#### Create an Agent

Find available agents on the Hub

```
surfkit find
```

Create a new agent

```
surfkit create agent -t pbarker/SurfPizza -n agent01
```

List running agents

```
surfkit list agents
```

#### Create a Device

Create an Ubuntu desktop for our agent to use.

```
surfkit create device --provider docker -n desktop01
```

List running devices

```
surfkit list devices
```

#### Solve a task

Use the agent to solve a task on the device

```
surfkit solve "Search for the most common variety of french duck" \
  --agent agent01 \
  --device desktop01
```

## Documentation

View our [documentation](https://docs.hub.agentsea.ai) for more in depth information.

## Usage

### Building Agents

Initialize a new project

```sh
surfkit new
```

Build a docker container for the agent

```sh
surfkit build
```

### Running Agents

Create an agent locally

```sh
surfkit create agent --name foo -t pbarker/SurfPizza
```

Create an agent on kubernetes

```sh
surfkit create agent --runtime kube -t pbarker/SurfPizza
```

List running agents

```sh
surfkit list agents
```

Get details about a specific agent

```sh
surfkit get agent foo
```

Fetch logs for a specific agent

```sh
surfkit logs foo
```

Delete an agent

```sh
surfkit delete agent foo
```

### Managing Devices

Create a device

```sh
surfkit create device --type desktop --provicer gce --name bar
```

List devices

```sh
surfkit list devices
```

View device in UI

```sh
surfkit view device bar
```

Delete a device

```sh
surfkit delete device bar
```

### Tracking Tasks

Create a tracker

```sh
surfkit create tracker
```

List trackers

```sh
surfkit list trackers
```

Delete a tracker

```sh
surfkit delete tracker foo
```

### Solving Tasks

Solve a task with an existing setup

```sh
surfkit solve "search for common french ducks" --agent foo --device bar
```

Solve a task creating the agent ad hoc

```sh
surfkit solve "search for alpaca sweaters" \
--device bar --agent-file ./agent.yaml
```

List tasks

```sh
surfkit list tasks
```

### Publishing Agents

Login to the hub

```sh
surfkit login
```

Publish the agent

```sh
surfkit publish
```

List published agent types

```sh
surfkit find
```

## Integrations

Skillpacks is integrated with:

- [MLLM](https://github.com/agentsea/mllm) A prompt management, routing, and schema validation library for multimodal LLMs
- [Taskara](https://github.com/agentsea/taskara) A task management library for AI agents
- [Skillpacks](https://github.com/agentsea/skillpacks) A library to fine tune AI agents on tasks.
- [Threadmem](https://github.com/agentsea/threadmem) A thread management library for AI agents

## Community

Come join us on [Discord](https://discord.gg/hhaq7XYPS6).

## Developing

Add the following function to your `~/.zshrc` (or similar)

```sh
function sk() {
  local project_dir="/path/to/surfkit/repo"
  local venv_dir="$project_dir/.venv"
  local ssh_auth_sock="$SSH_AUTH_SOCK"
  local ssh_agent_pid="$SSH_AGENT_PID"

  export SSH_AUTH_SOCK="$ssh_auth_sock"
  export SSH_AGENT_PID="$ssh_agent_pid"

  # Add the Poetry environment's bin directory to the PATH
  export PATH="$venv_dir/bin:$PATH"

  # Execute the surfkit.cli.main module using python -m
  surfkit "$@"
}
```

Replacing `/path/to/surfkit/repo` with the absolute path to your local repo.

Then calling `sk` will execute the working code in your repo from any location.

## Demonstrating the `surfkit` CLI for Educational Purposes

This section demonstrates how to use the `surfkit` CLI to create and manage agents and tasks, which can be used in educational presentations.

### Creating an Agent

To create an agent using the `surfkit` CLI, use the following command:

```sh
surfkit create agent --name my_agent --type pbarker/SurfPizza
```

### Listing Agents

To list all the agents, use the following command:

```sh
surfkit list agents
```

### Following Agent Logs

To follow the logs of an agent, use the following command:

```sh
surfkit logs agent my_agent --follow
```

## AI in Data Science for Educational Presentations

This section demonstrates how to use the `surfkit` toolkit to create AI agents for data analysis tasks, which can be used in educational presentations.

### Creating AI Agents for Data Analysis Tasks

To create an AI agent for data analysis tasks, use the following command:

```sh
surfkit create agent --name data_agent --type pbarker/DataAnalyzer
```

### Analyzing Datasets

To analyze a dataset using the AI agent, use the following command:

```sh
surfkit solve "Analyze the dataset for insights" --agent data_agent --device data_device
```

### Generating Insights

To generate insights from the analyzed data, use the following command:

```sh
surfkit solve "Generate insights from the analyzed data" --agent data_agent --device data_device
```

### Visualizing Data

To visualize the data using the AI agent, use the following command:

```sh
surfkit solve "Visualize the data" --agent data_agent --device data_device
```

## Demonstrating AI agent creation and management

This section demonstrates how to create, list, and manage AI agents using the `surfkit` CLI commands.

### Creating a New Agent

To create a new agent using the `surfkit` CLI, use the following command:

```sh
surfkit create agent --name new_agent --type pbarker/SurfPizza
```

### Listing Running Agents

To list all the running agents, use the following command:

```sh
surfkit list agents
```

### Managing Agents

To manage agents, use the following commands:

- To view the logs of an agent:

```sh
surfkit logs agent new_agent
```

- To delete an agent:

```sh
surfkit delete agent new_agent
```

- To get details about a specific agent:

```sh
surfkit get agent new_agent
```

## Teaching task solving with AI agents

This section demonstrates how to use the `solve` function from `surfkit/client.py` to solve tasks using AI agents.

### Creating Tasks

To create a task, use the following command:

```sh
surfkit create task --description "Search for information on AI in Data Science" --assigned-to new_agent
```

### Assigning Tasks to Agents

To assign a task to an agent, use the following command:

```sh
surfkit solve "Search for information on AI in Data Science" --agent new_agent --device data_device
```

### Explaining Parameters in the `solve` Function

The `solve` function in `surfkit/client.py` has the following parameters:

- `description`: Description of the task.
- `agent`: Name of the agent to use.
- `device`: Name of the device to use.
- `max_steps`: Maximum steps for the task.

### Examples of Tasks Solved by AI Agents

Here are some examples of tasks that can be solved by AI agents:

- Searching for information on AI in Data Science
- Performing specific actions on devices
