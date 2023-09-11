# Setup instructions

You will find below the instructions to set up your computer for [Le Wagon DevSecOps course](https://www.lewagon.com/)

A part of the setup will be done on your **local machine**, but most of the configuration will be done on a **Linux virtual machine already configured** containing all the tools you will need (Python, Docker, Terraform, and much more!).

Please **read the instructions carefully and execute all commands in the following order**.

Let's start :rocket:

## GitHub account

Have you signed up to GitHub? If not, [do it right away](https://github.com/join).

:point_right: **[Upload a picture](https://github.com/settings/profile)** and put your name correctly on your GitHub account. This is important as we'll use an internal dashboard with your avatar. Please do this **now**, before you continue with this guide.

## Connect to the Virtual Machine through SSH key

We want to safely communicate with your virtual machine using [SSH protocol](https://en.wikipedia.org/wiki/Secure_Shell). We need to generate an SSH key to authenticate.

- Open your terminal

<details>
  <summary markdown='span'>💡 Windows tip</summary>

We highly recommend installing [Windows Terminal](https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701?hl=fr-fr&gl=FR) from the Windows Store (installed on Windows 11 by default) to perform this operation
</details>

- Create an SSH key

<details>
  <summary markdown='span'>MacOS & Linux</summary>

```bash
ssh-keygen -t ed25519 -C lewagon
```

You should get the following message: `> Generating public/private algorithm key pair.`

- When you are prompted `> Enter file in which to save the key (/Users/username/.ssh/id_ed25519):`, press Enter
- You should be asked to `Enter a passphrase`, type a secure passphrase. It is like a password, but longer.

ℹ️ Don't worry if nothing prompts when you type, that is perfectly normal for security reasons.

- You should be asked to `Enter same passphrase again`, do it.

 The passphrase works with the key file to provide two-factor authentication. For this example, we're leaving the passphrase empty.

```text

Generating public/private ed25519 key pair.
Enter file in which to save the key (/Users/username/.ssh/id_ed25519):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /Users/username/.ssh/id_ed2ddd.
Your public key has been saved in /Users/username/.ssh/id_ed2ddd.pub.
The key fingerprint is:
SHA256:yJeb4MleZGDx0wQuUiakxqYb4AGThcnVF4uWgzva4LQ lewagon
The key's randomart image is:
+--[ED25519 256]--+
|+=oo+ +.o..      |
|=+ ..=o=.o       |
|..=..==.+ .      |
|o+. o+.+ o       |
|o+ o  + S        |
|oo= .o * o       |
|.E .  + +        |
|     . .         |
|      .          |
+----[SHA256]-----+
```

**❗️ You must remember this passphrase and the path of your private key.**

Now you have a public/private ed25519 key pair in the location specified. The `.pub` files are public keys, and files without an extension are private keys.

</details>

<details>
  <summary markdown='span'>Windows</summary>

To generate key files using the Ed25519 algorithm, run the following command from a PowerShell or cmd prompt on your client:

```bash
ssh-keygen.exe -t ed25519 -C lewagon
```

You should get the following message: `> Generating public/private algorithm key pair.`

- When you are prompted `> Enter file in which to save the key (C:\Users\username\.ssh\id_ed25519):`, press Enter
- You should be asked to `Enter a passphrase`, type a secure passphrase, it is like a password, but longer.

ℹ️ Don't worry if nothing prompt when you type, that is perfectly normal for security reasons.

- You should be asked to `Enter same passphrase again`, do it.

 The passphrase works with the key file to provide two-factor authentication. For this example, we're leaving the passphrase empty.

```text
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in C:\Users\username\.ssh\id_ed25519.
Your public key has been saved in C:\Users\username\.ssh\id_ed25519.pub.



The key fingerprint is:
SHA256:OIzc1yE7joL2Bzy8!gS0j8eGK7bYaH1FmF3sDuMeSj8 lewagon

The key's randomart image is:
+--[ED25519 256]--+
|        .        |
|         o       |
|    . + + .      |
|   o B * = .     |
|   o= B S .      |
|   .=B O o       |
|  + =+% o        |
| *oo.O.E         |
|+.o+=o. .        |
+----[SHA256]-----+
```

**❗️ You must remember this passphrase and the path of your private key.**

Now you have a public/private ed25519 key pair in the location specified. The `.pub` files are public keys, and files without an extension are private keys.

</details>

### Upload public KEY

Let's now send your public key to the LeWagon Engineering team so that we can place it on the Virtual Machine we will provide to you. Once it is done, you'll be able to connect to it through SSH.

- In your terminal, copy your public SSH key

<details>
  <summary markdown='span'>MacOs & Linux </summary>

```bash
cat < ~/.ssh/id_ed25519.pub
# <Display the content of the id_ed25519.pub file. Replace ~/.ssh/id_ed25519.pub with your public key path
```

Copy the output.

```ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOkPUdnhB5beA8vzNXbCMz0RJIFISrcm96ZXrfzhtYLO lewagon```

</details>

<details>
  <summary markdown='span'>Windows</summary>

With Windows PowerShell

```bash
Get-Content -Path $env:USERPROFILE\.ssh\id_ed25519.pub
# Display the content of the id_ed25519.pub file. Replace id_ed25519.pub with your public key path
```

Copy the output. It should look like this ```ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOkPUdnhB5beA8vzNXbCMz0RJIFISrcm96ZXrfzhtYLO lewagon```

In case you have any issues, feel free to refer to this [section](<https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_keymanagement>)

</details>

- Upload SSH key on Google Form

Fill this [Google Form](https://forms.gle/KaK6q3mN9NwVipds7)  so our Engineering team can assign you a virtual machine.
Answer the questions by filling out your name, email, and public key you just created.

 Make sure that the public keys match this pattern :

 ```bash
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AzNXbCMz0RJIFISrcm96ZXrfzhtYLO lewagon
```

 Please wait a few minutes and check your email box. You should receive an email with your VM's IP address once it is ready! Please, ask for help if you are stuck here.

## Connect to the VM through VS Code

_Note: The following section requires you already have received the VM provisioning confirmation as well as the IP address of the VM we assigned you with.

## Visual Studio Code

### Installation

Have you installed VSCode already? If not, let's install [Visual Studio Code](https://code.visualstudio.com) text editor.

- Go to [Visual Studio Code download page](https://code.visualstudio.com/download).
- Click on "Windows" button
- Open the file you have just downloaded.
- Install it with few options:

![VS Code installation options](https://github.com/lewagon/setup/blob/master/images/windows_vscode_installation.png)

When the installation is finished, launch VS Code.

### VS Code Remote SSH Extension

We need to connect VS Code to a virtual machine in the cloud, so you will only work on that machine during the bootcamp. A pretty helpful [**Remote SSH Extension**](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) is available on the VS Code Marketplace.

- Open VS Code > Open the [command palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) > Type `Extensions: Install Extensions`

<img alt="VSCode extensions - Search - Remote" src="https://wagon-public-datasets.s3.amazonaws.com/data-engineering/setup/vscode-extensions-search-remote.png" width=500>

- Install the extension

<img alt="VS Code extensions - Remote - Details" src="https://wagon-public-datasets.s3.amazonaws.com/data-engineering/setup/vscode-extensions-remote.png" width=500>

That's the only extension you should install on your _local_ machine, we will install additional VS Code extensions on your _virtual machine_.

### Virtual Machine connexion

- Open VS Code > Open the [command palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) > Type `Remote-SSH: Connect to Host...`

<img alt="vscode-connect-to-host" src="https://wagon-public-datasets.s3.amazonaws.com/data-engineering/setup/vscode-connect-to-host.png" width=500>

- Click on `Add a new host`
- Type `ssh -i <path/to/your/private/key> lewagon@<ip address>`, for instance, with private key at `~/.ssh/ed25519`, with a public IP of `34.77.50.76`, I'll type `ssh -i ~/.ssh/ed25519 lewagon@34.77.50.76` for a Mac/Linux machine and `ssh -i C:\Users\username\.ssh\id_ed25519 lewagon@34.77.50.76` for a Windows one.

<img alt="vscode-ssh-connection-command" src="https://wagon-public-datasets.s3.amazonaws.com/data-engineering/setup/vscode-ssh-connection-command.png" width=500>

- When prompted to `Select SSH configuration file to update`, pick the one in your home directory, under the `.ssh` folder, `~/.ssh/config` basically. Usually VS Code will automatically pick the best option, so their default should work.

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

**The setup of your local machine is over. All following commands will be run from within your 🚨 virtual machine**🚨 terminal

---

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

First, to **login**, copy-paste the following command in your terminal:

:warning: **DO NOT edit the `email`**

```bash
gh auth login -s 'user:email' -w
```

gh will ask you few questions:

`What is your preferred protocol for Git operations?` With the arrows, choose `SSH` and press `Enter`. SSH is a protocol to log in using SSH keys instead of the well-known username/password pair.

`Generate a new SSH key to add to your GitHub account?` Press `Enter` to ask gh to generate your SSH keys.

Type something you want and that you'll remember. `Enter a passphrase for your new SSH key (Optional)`. It's a password to protect your private key stored on your hard drive. Then press `Enter`.

:warning: When you type your passphrase, nothing will show up on the screen, **that's normal**. This is a security feature to mask not only your passphrase as a whole but also its length. Just type your passphrase and when you're done, press `Enter`.

You will then get the following output:

```bash
! First copy your one-time code: 0EF9-D015
- Press Enter to open github.com in your browser...
```

Select and copy the code (`0EF9-D015` in the example), then press `Enter`.

Your browser will open and ask you to authorize GitHub CLI to use your GitHub account. Accept and wait a bit.

Come back to the terminal, press `Enter` again, and that's it.

To check that you are correctly connected, type:

```bash
gh auth status
```

:heavy_check_mark: If you get `Logged in to github.com as <YOUR USERNAME>`, then all good :+1:

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

It's essential to use the same email as the one you use on [GitHub](https://github.com/settings/emails) so that [commits are linked to your profile](https://help.github.com/articles/why-are-my-commits-linked-to-the-wrong-user/#commits-are-not-linked-to-any-user).

## Exercises

The repository which you just forked contains all the exercises for the week. To work on them, clone them on your the VM. Run:

```bash
mkdir -p ~/code/<user.github_nickname> && cd $_
gh repo fork git@github.com:lewagon/devsecops-challenges.git --remote=false
cd devsecops-challenges
git remote add upstream git@github.com:lewagon/devsecops-challenges.git
pwd # This is your exercise repository!
```

This repository has a `Pipfile`. You can now easily install dependencies with the following command:

```bash
pipenv install --dev # to install `packages` **and** `dev-packages`
```

It will create the Virtualenv for this folder, using Python 3.8 as [specified](https://github.com/lewagon/reboot-python/blob/master/Pipfile#L15-L16)

## Azure

### Join the Azure Organization and put credentials in the VM 🔑

Everyone should recieve an email with object "DevSecOps formation Azure Credentials" containing the instructions to join our Azure organization along with your credentials for Azure access.

<img alt="aws-credentials" src="https://wagon-devsecops.s3.eu-west-3.amazonaws.com/img/aws-credentials.png">

First, log in to your account on the console.

Click on the [link](910402161650.signin.aws.amazon.com/console) and fill the sections with the **username** and temporary **password** we provide you in the mail.

When connecting for the first time on the console users will be asked to change their passwords.

Once it is done, you can now put your aws credentials in the virtual machine to ensure you can also access to aws through the cli.

To configure the credentials using the command line all you have to do is open a terminal in VSCode in your Virtual Machine environement and type

```bash
azure login
```

When you use the azure CLI to log in to Azure, it automatically stores information and credentials in a directory on your machine. You don't  need to worry about managing this as it is handled for you.

Windows: `%USERPROFILE%\.azure`
macOS and Linux: `~/.azure`


## Further notes about your VM

The virtual machine  you will work with is a Linux Ubuntu machine with the following tools installed :

- Python 3.8.6 with pipenv
- Docker & Docker Compose
- Kubernetes
- Terraform
- Azure CLI
- Github CLI

The default shell is `zsh`, an extension over the bourne shell.
There is no need to start or stop the VM at the end/beginning of each day. We will do that for you.

See you soon!
