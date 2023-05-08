# 0x17. Web stack debugging #3
 
<img width="520"  alt="image"  src="https://www.google.com/url?sa=i&url=https%3A%2F%2Ftenor.com%2Fsearch%2Fdebugging-gifs&psig=AOvVaw1k7NN2NHZZlzfnd5AGmvNg&ust=1683673006798000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCPD--YHp5v4CFQAAAAAdAAAAABAE">
 
## Contents:open_file_folder:
 
- Project Description:newspaper:
- General Objectives:bulb:
- Instalation:wrench:
- Tasks:clipboard:
- Built with:hammer:
- Resources:books:
- Author:black_nib:
 
---
 
## Project Description:newspaper:
 
When debugging, sometimes logs are not enough. Either because the software is breaking in a way that was not expected and the error is not being logged, or because logs are not providing enough information. In this case, you will need to go down the stack, the good news is that this is something Holberton students can do :)

Wordpress is a very popular tool, it allows you to run blogs, portfolios, e-commerce and company websites… It actually powers 26% of the web, so there is a fair chance that you will end up working with it at some point in your career.

Wordpress is usually run on LAMP (Linux, Apache, MySQL, and PHP), which is a very widely used set of tools.

The web stack you are debugging today is a Wordpress website running on a LAMP stack.
 
---
 
## General Objectives:bulb:
---
 
## Tasks:clipboard:
 
### [0. Strace is your friend ]
* Using strace, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing).

Hint:

strace can attach to a current running process
You can use tmux to run strace in one window and curl in another one
Requirements:

Your 0-strace_is_your_friend.pp file must contain Puppet code
You can use whatever Puppet resource type you want for you fix

---

## Built with:hammer:

* Puppet
 
---
 
## Resources:books:
 

* [Web Server](https://intranet.hbtn.io/concepts/17)
* [Web stack debugging](https://intranet.hbtn.io/concepts/68)
 
---
