# Setup instructions

You will find below the instructions to set up your computer for [Le Wagon DevSecOps course](https://www.lewagon.com/)

A part of the setup will be done on your **local machine** but most of the configuration will be done on a **virtual machine already configured** containing with all the tools you will need (Python, Docker, Terraform, and much more!).

Please **read instructions carefully and execute all commands in the following order**.

Let's start :rocket:

## GitHub account

Have you signed up to GitHub? If not, [do it right away](https://github.com/join).

:point_right: **[Upload a picture](https://github.com/settings/profile)** and put your name correctly on your GitHub account. This is important as we'll use an internal dashboard with your avatar. Please do this **now**, before you continue with this guide.


## Connect to the Virtual Machine through SSH key

We want to safely communicate with your virtual machine using [SSH protocol](https://en.wikipedia.org/wiki/Secure_Shell). We need to generate a SSH key to authenticate.

- Open your terminal

<details>
  <summary markdown='span'>💡 Windows tip</summary>

We highly recommend installing [Windows Terminal](https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701?hl=fr-fr&gl=FR) from the Windows Store (installed on Windows 11 by default) to perform this operation
</details>

- Create a SSH key

<details>
  <summary markdown='span'>MacOS & Linux</summary>

```bash
EMAIL="your_email@example.com" # replace with your github account email
ssh-keygen -t ed25519 -C $EMAIL
```

</details>

<details>
  <summary markdown='span'>Windows</summary>

```bash
EMAIL="your_email@example.com" # replace with your github account email
ssh-keygen.exe -t ed25519 -C $EMAIL
```
</details>

You should get the following message: `> Generating public/private algorithm key pair.`
- When you are prompted `> Enter a file in which to save the key`, press Enter
- You should be asked to `Enter a passphrase`, type a secure passphrase, it is like a password, but longer.

ℹ️ Don't worry if nothing prompt when you type, that is perfectly normal for security reasons.

- You should be asked to `Enter same passphrase again`, do it.

**❗️ You must remember this passphrase.**


### Upload public KEY

- In your terminal, copy your public SSH key

<details>
  <summary markdown='span'>MacOs & Linux</summary>

```bash
pbcopy < ~/.ssh/id_ed25519.pub
# Copies the contents of the id_ed25519.pub file to your clipboard
```

</details>

<details>
  <summary markdown='span'>Windows</summary>

```bash
clip < ~/.ssh/id_ed25519.pub
# Copies the contents of the id_ed25519.pub file to your clipboard
```
</details>


#### Option A - Upload SSH key on GitHub

- 1. On GitHub.com In the upper-right corner of any page, click your profile photo, then click Settings.

<img alt="VSCode extensions - Search - Remote" src="https://docs.github.com/assets/cb-139735/mw-1000/images/help/settings/userbar-account-settings.webp" height=400 width=300>


- 2. In the "Access" section of the sidebar, click 🔑 SSH and GPG keys.

- 3. Click **New SSH key** or **Add SSH key**.

<img alt="VSCode extensions - Search - Remote" src="https://docs.github.com/assets/cb-28257/mw-1000/images/help/settings/ssh-add-ssh-key-with-auth.webp" width=500>

- 3. In the "Title" field, add a descriptive label for the new key. For example, if you're using a professional laptop, you might call this key "Professional laptop".

- 5. Select the type of key, either authentication or signing. For more information about commit signing, see "About commit signature verification."

- 6. Paste your public key into the "Key" field.

<img alt="VSCode extensions - Search - Remote" src="https://docs.github.com/assets/cb-47495/mw-1000/images/help/settings/ssh-key-paste-with-type.webp" width=500>

- 7. Click **Add SSH key**

<img alt="VSCode extensions - Search - Remote" src="https://docs.github.com/assets/cb-6592/mw-1000/images/help/settings/ssh-add-key.webp" width=500>

- 8. If prompted, confirm access to your account on GitHub. For more information, see "Sudo mode."


#### Option B - Upload SSH key on Google Form

<!-- TODO with LeWagon Engineering Team -->



## Confirm  Virtual Machine provisioning and retrieve IP address


_Note: The following section requires you already have a [GitHub](https://github.com/) account and that you have generated an SSH key & upload the public key already.

<!-- TODO with LeWagon Engineering Team -->

<!-- In this section, we should let students know what will happen now (wait a few minutes for VM provioning before receiving an email with the IP adress?) -->


## Visual Studio Code

### Installation

Let's install [Visual Studio Code](https://code.visualstudio.com) text editor.

- Go to [Visual Studio Code download page](https://code.visualstudio.com/download).
- Click on "Windows" button
- Open the file you have just downloaded.
- Install it with few options:

![VS Code installation options](https://github.com/lewagon/setup/blob/master/images/windows_vscode_installation.png)

When the installation is finished, launch VS Code.


### VS Code Remote SSH Extension

We need to connect VS Code to a virtual machine in the cloud so you will only work on that machine during the bootcamp. A pretty useful [**Remote SSH Extension**](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) is available on the VS Code Marketplace.

- Open VS Code > Open the [command palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) > Type `Extensions: Install Extensions`

<img alt="VSCode extensions - Search - Remote" src="https://wagon-public-datasets.s3.amazonaws.com/data-engineering/setup/vscode-extensions-search-remote.png" width=500>

- Install the extension

<img alt="VS Code extensions - Remote - Details" src="https://wagon-public-datasets.s3.amazonaws.com/data-engineering/setup/vscode-extensions-remote.png" width=500>

That's the only extension you should install on your _local_ machine, we will install additional VS Code extensions on your _virtual machine_.

### Virtual Machine connexion

- Open VS Code > Open the [command palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) > Type `Remote-SSH: Connect to Host...`

<img alt="vscode-connect-to-host" src="https://wagon-public-datasets.s3.amazonaws.com/data-engineering/setup/vscode-connect-to-host.png" width=500>

- Click on `Add a new host`
- Type `ssh -i <path/to/your/private/key> <username>@<ip address>`, for instance, my username is `somedude`, and private key at `~/.ssh/id_rsa`, with a public IP of `34.77.50.76`, I'll type `ssh -i ~/.ssh/id_rsa somedude@34.77.50.76`

<img alt="vscode-ssh-connection-command" src="https://wagon-public-datasets.s3.amazonaws.com/data-engineering/setup/vscode-ssh-connection-command.png" width=500>


- When prompted to `Select SSH configuration file to update`, pick the one in your home directory, under the `.ssh` folder, `~/.ssh/config` basically. Usually VS Code will pick automatically the best option, so their default should work.

<img alt="vscode-add-host-ssh-config" src="https://wagon-public-datasets.s3.amazonaws.com/data-engineering/setup/vscode-add-host-ssh-config.png" width=500>

- You should get a pop-up on the bottom right notifying you the host has been added

<img alt="vscode-host-added" src="https://wagon-public-datasets.s3.amazonaws.com/data-engineering/setup/vscode-host-added.png" width=500>

- Open again the [command palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) > Type `Remote-SSH: Connect to Host...` > Pick your VM IP address

<img alt="vscode-add-new-host" src="https://wagon-public-datasets.s3.amazonaws.com/data-engineering/setup/vscode-add-new-host.png" width=500>

- The first time, VSCode might ask you for a security permission like below, say yes / continue.

<img alt="vscode-remote-connection-confirm" src="https://wagon-public-datasets.s3.amazonaws.com/data-engineering/setup/vscode-remote-connection-confirm.png" width=500>

- Open again the [command palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) > Type `Terminal: Create New Terminal (in active workspace)` > You now have a Bash terminal in your virtual machine!

<img alt="vscode-command-palette-new-terminal" src="https://wagon-public-datasets.s3.amazonaws.com/data-engineering/setup/vscode-command-palette-new-terminal.png" width=500>
<br>
<img alt="vscode-terminal" src="https://wagon-public-datasets.s3.amazonaws.com/data-engineering/setup/vscode-terminal.png" width=500>

- Still on your *local* computer, lets create a more readable version of your machine to connect to!

```bash
code ~/.ssh/config
```

You should see something like the following:

```bash
Host <machine ip>
  HostName <machine ip>
  IdentityFile <file path for your ssh key>
  User <username>
```
You can now change Host to whatever you would like to see as the name of your connection or in terminal with `ssh <Host>`!

```bash
# For instance
Host "devsecops bootcamp"
  HostName 35.240.107.210
  IdentityFile <file path for your ssh key>
  User <username>
```

**The setup of your local machine is over. All following commands will be run from within your 🚨 virtual machine**🚨 terminal (via VS code for instance)


## VS Code Extensions

Let's install some useful extensions to VS Code.

- Open your VS Code instance and make sure you're connected to the remote server. At the bottom left, you'll see:

<img alt="vscode-ssh" src="https://wagon-public-datasets.s3.amazonaws.com/data-engineering/setup/vscode-ssh.png" width=500>

- Open the VS Code terminal (`CMD` + `` ` `` or `CTRL` + `` ` ``) then run the following commands:

```bash
code --install-extension ms-vscode.sublime-keybindings
code --install-extension emmanuelbeziat.vscode-great-icons
code --install-extension ms-python.python
code --install-extension KevinRose.vsc-python-indent
code --install-extension ms-python.vscode-pylance
code --install-extension redhat.vscode-yaml
code --install-extension ms-azuretools.vscode-docker
```

Here is a list of the extensions you are installing:
- [Sublime Text Keymap and Settings Importer](https://marketplace.visualstudio.com/items?itemName=ms-vscode.sublime-keybindings)
- [VSCode Great Icons](https://marketplace.visualstudio.com/items?itemName=emmanuelbeziat.vscode-great-icons)
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Python Indent](https://marketplace.visualstudio.com/items?itemName=KevinRose.vsc-python-indent)
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- [YAML](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml)
- [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)


## GitHub CLI

CLI is the acronym of [Command-line Interface](https://en.wikipedia.org/wiki/Command-line_interface).

In this section, we will use [GitHub CLI](https://cli.github.com/) to interact with GitHub directly from the terminal.

It should already be installed on your virtual machine.

First in order to **login**, copy-paste the following command in your terminal:

:warning: **DO NOT edit the `email`**

```bash
gh auth login -s 'user:email' -w
```

gh will ask you few questions:

`What is your preferred protocol for Git operations?` With the arrows, choose `SSH` and press `Enter`. SSH is a protocol to log in using SSH keys instead of the well known username/password pair.


`Generate a new SSH key to add to your GitHub account?` Press `Enter` to ask gh to generate the SSH keys for you.

`Enter a passphrase for your new SSH key (Optional)`. Type something you want and that you'll remember. It's a password to protect your private key stored on your hard drive. Then press `Enter`.

:warning: When you type your passphrase, nothing will show up on the screen, **that's normal**. This is a security feature to mask not only your passphrase as a whole but also its length. Just type your passphrase and when you're done, press `Enter`.

You will then get the following output:

```bash
! First copy your one-time code: 0EF9-D015
- Press Enter to open github.com in your browser...
```

Select and copy the code (`0EF9-D015` in the example), then press `Enter`.

Your browser will open and ask you to authorize GitHub CLI to use your GitHub account. Accept and wait a bit.

Come back to the terminal, press `Enter` again, and that's it.

To check that you are properly connected, type:

```bash
gh auth status
```

:heavy_check_mark: If you get `Logged in to github.com as <YOUR USERNAME> `, then all good :+1:

To check if this step is done, run:

```bash
ssh -T git@github.com
```
To check if this step is done, run:

```bash
ssh -T git@github.com
```

If it says "Permission denied", call a teacher to help you. If it says "Hi <github_nickname>", all good!

At last, we need to configure the local `git` command to tell it who you are when you make a commit:

```bash
git config --global user.email "your_github_email@domain.com"
git config --global user.name "Your Full Name"
```

It's important to use the same email as the one you use on [GitHub](https://github.com/settings/emails) so that [commits are linked to your profile](https://help.github.com/articles/why-are-my-commits-linked-to-the-wrong-user/#commits-are-not-linked-to-any-user).

## Exercises

The repository which you just forked contains all the exercises for the week. To work on them, clone them on your the VM. Still in Git Bash, run:

```bash
mkdir -p ~/code/<user.github_nickname> && cd $_
gh repo fork git@github.com:lewagon/devsecops-challenges.git --remote=false
cd devsecops-challenges
git remote add upstream git@github.com:lewagon/devsecops-challenges.git
pwd # This is your exercise repository!
```

This repository has a `Pipfile`. You now can easily install dependencies with the following command:

```bash
pipenv install --dev # to install `packages` **and** `dev-packages`
```

It will create the Virtualenv for this folder, using Python 3.8 as [specified](https://github.com/lewagon/reboot-python/blob/master/Pipfile#L15-L16)



## AWS

### Add a service account key 🔑


<!-- TODO with OnePoint -->

