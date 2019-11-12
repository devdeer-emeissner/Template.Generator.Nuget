import subprocess
import json
import os


def ReadJsonFile(path):
    with open(path, "r") as file:
        jsdata = file.read().replace('\n', '')
    return jsdata


def ProcessDotnetInstructions(dotnet):
    if "solution" in dotnet:
        CreateSolution(dotnet["solution"]["parameters"])
    if "projects" in dotnet:
        for command in dotnet["new"]:
            CreateProject(command)


def ProcessAzureInstructions(azure):
    return


def CreateSolution(params):
    temp = ["dotnet", "new", "sln"] + ProcessParams(params)
    subprocess.run(temp)


def ProcessParams(params):
    result = []
    for param in params:
        temp = param.split()
        for item in temp:
            result.append(item)
    return result


def CreateProject(project):
    return


def main():
    if "dotnet" in data:
        ProcessDotnetInstructions(data["dotnet"])
    elif "azure" in data:
        ProcessAzureInstructions(data["azure"])


data = json.loads(ReadJsonFile("project.config"))


if __name__ == "__main__":
    main()