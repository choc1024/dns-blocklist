# Updates
<details>
	<summary>Expand</summary>
	<ul>
		System upgrade: OK, the script is almost finished, and I somehow managed to setup Cron in my Arch Linux and schedule it to auto compile everything every 3 hours. This should be much better and easier than doing "cd ~/Code/dns-blocklist && python autoCompile.py" every so often.
	</ul>
</details>


# Trust me bro
It looks like most people here just don't trust this. But seriously... why would I redirect you to malicious IPs? Also, there is no way to do so, because everything is in ABP format, which does not support this. Still don't believe me? Then use RegExp (Regular Expressions, aka regex) to search for IPv4 and IPv6 IPs in the blocklist. There is none.

# Description
DNS Blocklists compiled by me. They are a unification of a bunch of blocklists made by other people. Also, if you find it usefull or like it, please spread the word and star this repo!

Please read CHANGELOG.md

To reduce the possibilities of a takedown (e.g. servers hit by meteorites, alien invasion...), this blocklist is hosted both on [GitHub](https://github.com/choc1024/dns-blocklist) and [GitLab](https://gitlab.com/choc1024/dns-blocklist)

# FAQ
<details>
  <summary>Which software are currently supported?</summary>
  <ul>
    <p>The blocklist is currently compiled for AdGuard Home. Support for pihole will probably not be added as PiHole uses a hosts-format, allowing malicious actors to add malicious IPs. But AdGuard Home uses ABP (AdBlock Plus) formar, which means that this will also work with most if not all ad blockers. Sorry, Pi-Hole!</p>
  </ul>
</details>
<details>
  <summary>Which blocklists are included?</summary>
  <ul>
    <p>Scroll down</p>
  </ul>
</details>
<details>
  <summary>How do I use it?</summary>
  <ul>
    <p>Open your AdGuard Home interface, go to Filters > DNS Blocklists, click "Add Blocklist", select "Add Custom List" and then give it the title you want and copy paste this URL: https://github.com/choc1024/dns-blocklist/raw/main/latest/latest.txt OR this alternative mirror URL: https://gitlab.com/choc1024/dns-blocklist/-/raw/main/latest/latest.txt. Or just DuckDuckGo it for more info.</p>
  </ul>
</details>
<details>
  <summary>It is too aggressive at blocking</summary>
  <ul>
    <p>It shouldn't be, but uh... just whitelist the domains you want? I guess that blocking too much is still better than not having false-positives and letting tracking and malware domains pass...</p>
  </ul>
</details>

# Blocklists Included
| Name | Status in Main Blocklist | URL |
|------|-------|------|
| HaGeZi's Pop-Up Ads | 🟢 Enabled | https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/popupads.txt |
| AdGuard Default DNS filter | 🟢 Enabled | https://adguardteam.github.io/HostlistsRegistry/assets/filter_1.txt | 
| AdAway Default Blocklist | 🟢 Enabled | https://raw.githubusercontent.com/AdAway/adaway.github.io/master/hosts.txt |  
| Stalkerware Indicators List | 🟢 Enabled | https://github.com/AssoEchap/stalkerware-indicators/raw/master/generated/hosts_full | 
| AdGuard DNS Popup Hosts filter | 🟢 Enabled | https://adguardteam.github.io/HostlistsRegistry/assets/filter_59.txt | 
| Dan Pollock's List | 🟢 Enabled | https://someonewhocares.org/hosts/zero/hosts |  
| AWAvenue Ads Rule | 🟢 Enabled | https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/AWAvenue-Ads-Rule.txt | 
| HaGeZi's Ultimate Blocklist | 🟢 Enabled | https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/ultimate.txt | 
| OISD Blocklist Big | 🟢 Enabled | https://big.oisd.nl/ | 
| Peter Lowe's Blocklist | 🟢 Enabled | https://pgl.yoyo.org/adservers/serverlist.php?hostformat=adblockplus&showintro=1&mimetype=plaintext | 
| Steven Black's List | 🟢 Enabled | https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts |  
| HaGeZi's Allowlist Referral | 🔴 Disabled | https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/whitelist-referral.txt | 
| Dandelion Sprout Anti Push Notifications | 🟢 Enabled | https://raw.githubusercontent.com/DandelionSprout/adfilt/master/AdGuard%20Home%20Compilation%20List/AdGuardHomeCompilationList-Notifications.txt | 
| Malicious URL Blocklist (URLHaus) | 🟢 Enabled | https://malware-filter.gitlab.io/malware-filter/urlhaus-filter-agh.txt | 
| ShadowWhisperer's Dating List | 🟢 Enabled | https://raw.githubusercontent.com/ShadowWhisperer/BlockLists/master/Lists/Dating | 
| NoCoin Filter List | 🟢 Enabled | https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/hosts.txt |  
| Phishing Army | 🟢 Enabled | https://phishing.army/download/phishing_army_blocklist_extended.txt |  
| Phishing URL Blocklist (PhishTank and OpenPhish) | 🟢 Enabled | https://adguardteam.github.io/HostlistsRegistry/assets/filter_30.txt | 
| HaGeZi's The World's Most Abused TLDs | 🟢 Enabled | https://adguardteam.github.io/HostlistsRegistry/assets/filter_56.txt | 
| HaGeZi's Threat Intelligence Feeds (TIF) | 🟢 Enabled | https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/tif.txt | 
| Dandelion Sprout's Anti-Malware List | 🟢 Enabled | https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareAdGuardHome.txt | 
| HaGeZi's DynDNS Blocklist | 🟢 Enabled | https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/dyndns.txt | 
| HaGeZi's Encrypted DNS/VPN/TOR/Proxy Bypass | 🟢 Enabled | https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/doh-vpn-proxy-bypass.txt | 
| The Blocklist Project Ads | 🟢 Enabled | https://blocklistproject.github.io/Lists/adguard/ads-ags.txt | 
| The Blocklist Project Tracking | 🟢 Enabled | https://blocklistproject.github.io/Lists/adguard/tracking-ags.txt | 
| The Blocklist Project Porn | 🟢 Enabled | https://blocklistproject.github.io/Lists/adguard/porn-ags.txt | 
| HaGeZi's Popup Ads | 🟢 Enabled | https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/popupads.txt | 
| ph00lt0 Blocklist Unified | 🟢 Enabled | https://raw.githubusercontent.com/ph00lt0/blocklists/master/blocklist.txt | 
| 1Hosts Pro | 🟢 Enabled | https://cdn.jsdelivr.net/gh/badmojr/1Hosts@master/Pro/adblock.txt | 
| EasyList AdServers | 🟢 Enabled | https://github.com/easylist/easylist/raw/master/easylist/easylist_adservers.txt | 
| EasyList Allowlist | 🔴 Disabled | https://github.com/easylist/easylist/raw/master/easylist/easylist_allowlist.txt | 
| EasyList Third Party | 🟢 Enabled | https://github.com/easylist/easylist/raw/master/easylist/easylist_thirdparty.txt | 
| EasyPrivacy Tracking Servers | 🟢 Enabled | https://github.com/easylist/easylist/raw/master/easyprivacy/easyprivacy_trackingservers.txt | 
| EasyPrivacy Tracking Servers Third Party | 🟢 Enabled | https://github.com/easylist/easylist/raw/master/easyprivacy/easyprivacy_trackingservers_thirdparty.txt | 
| EasyPrivacy Tracking Servers Notifications | 🟢 Enabled | https://github.com/easylist/easylist/raw/master/easyprivacy/easyprivacy_trackingservers_notifications.txt | 
| EasyPrivacy Tracking Servers Mining | 🟢 Enabled | https://github.com/easylist/easylist/raw/master/easyprivacy/easyprivacy_trackingservers_mining.txt | 
| EasyPrivacy Tracking Servers International | 🟢 Enabled | https://github.com/easylist/easylist/raw/master/easyprivacy/easyprivacy_trackingservers_international.txt | 
| EasyPrivacy Tracking Servers General | 🟢 Enabled | https://github.com/easylist/easylist/raw/master/easyprivacy/easyprivacy_trackingservers_general.txt |
| Choco's Allowlist (Handmade by me :) | 🟢 Enabled | In the repository |

# Unblocking Rules

If you are the owner of a website or service and it has been blocked by this blocklist, you can open an issue in this repo and I will look into it as soon as possible.

I will NOT remove the rule if your website or service:

- Provides Ads, Tracking, Malware, Crypto Mining, Phishing, etc.
- Has Ads, Tracking, Malware, Crypto Mining, Phishing, etc.

If your website contains pirated content, then:

- IF it is not popular enough or does not have a good enough reputation, it won't be unblocked.
- IF it has Malware, it won't be unblocked.

Reasons that WILL make me unblock your website or service:

- It is a legit service that serves content (CDN)
- Blocking it will break other websites (e.g. CloudFlare)

If you open an issue wanting me to unblock your website or service, then the issue MUST contain:

- The Name, URL and IP of the host
- The EXACT use of that website (What it is for)
- WHY should I unblock it
- What are the potential consequences of blocking it (do websites break?)

If you are NOT the owner of that website or service, you can still request to unblock one.

# Pros and Cons of using a unified list

## Pros
- In a unified list, all duplicate rules are automatically removed and normally, all rules are optimized. Which means that it is more lightweight. Take this blocklist for example. If we sum up all of the rules in every blocklist individually, it is around 2~3 million. But after unifying them, we get just a bit more than 1.5 million rules.
- It is easier to add just 1 big blocklist than adding a bunch of smaller blocklists one by one and having to search their URLs.
- For a software (like AdGuard Home) to update the blocklists, it is more helpful as it just needs to download a single blocklist rather than checking a dozen.
## Cons
- A unified Blocklist contains ALL rules of a dozen of blocklists, which removes the possibility of blocking only a specific type of websites (e.g., only blocking malware instead of malware AND ads, trackers, phishing, etc.)

# Compiling

## Prerequesites

- NPM
- Internet
- Git

## Steps

1. Install [hostlist-compiler](https://github.com/AdguardTeam/HostlistCompiler) using NPM:
```
npm i -g @adguard/hostlist-compiler
```
2. Clone this repo using git:
```
git clone https://github.com/choc1024/dns-blocklist.git
cd dns-blocklist/latest
```
3. Compile:
```
hostlist-compiler -c config.json -o myCustomBlocklist.txt
```
Please note that the compilation may take a few minutes (for me it took half an hour). It is recommended to let it run in the background while you do other things. 

# Notice

I am currently working on a script that automatically compiles everything and updates them to github REGULARLY, but it is not complete (yet), and until then everything will be compiled manually every day (or so).
Update: The script is finished.

## GitLab and GitHub

The blocklist has been uploaded to both GitLab AND GitHub, but GitHub is the RECOMMENDED source because it I mainly upload all updates to it (the script may fix it but IDK).
