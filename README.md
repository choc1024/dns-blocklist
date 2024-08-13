# Table of Contents
- [Description](https://github.com/choc1024/dns-blocklist?tab=readme-ov-file#description)
- [FAQ](https://github.com/choc1024/dns-blocklist?tab=readme-ov-file#faq)
- [Blocklists Included](https://github.com/choc1024/dns-blocklist?tab=readme-ov-file#blocklists-included)
- [Unblocking Rules](https://github.com/choc1024/dns-blocklist?tab=readme-ov-file#unblocking-rules)
- [Pros and Cons of using a unified list](https://github.com/choc1024/dns-blocklist?tab=readme-ov-file#pros-and-cons-of-using-a-unified-list)
  - [Pros](https://github.com/choc1024/dns-blocklist?tab=readme-ov-file#pros)
  - [Cons](https://github.com/choc1024/dns-blocklist?tab=readme-ov-file#cons)
- [Compiling](https://github.com/choc1024/dns-blocklist?tab=readme-ov-file#compiling)
  - [Prerequesites](https://github.com/choc1024/dns-blocklist?tab=readme-ov-file#prerequesites)
  - [Steps](https://github.com/choc1024/dns-blocklist?tab=readme-ov-file#steps)

# Description
DNS Blocklists compiled by me. They are a unification of a bunch of blocklists made by other people. Also, if you find it usefull or like it, please spread the word and star this repo!

Also, PLEASE READ THE CHANGELOG.MD FILE!!! NOTICE: To reduce the posibilities of the blocklist being unavailable (e.g., GitHub servers hit by a meteorite or Microsoft taking down this repo), I have made a mirror of the repo at [GitLab](https://gitlab.com/choc1024/dns-blocklist/). 

# FAQ
<details>
  <summary>Which software are currently supported?</summary>
  <ul>
    <p>The blocklist is currently compiled for AdGuard Home, IDK if it will work on e.g. PiHole. I guess it should work on most adblockers though.</p>
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
  <summary>When Are you Going to add support for other software??</summary>
  <ul>
    <p>When I have enough time. But you can always fork this repo and do it yourself.</p>
  </ul>
</details>
<details>
  <summary>It is too aggressive at blocking</summary>
  <ul>
    <p>I am working on that right now.</p>
  </ul>
</details>

# Blocklists Included
| Name | Status in Main Blocklist | URL |
|------|-------|------|
| AdGuard Default DNS filter | 🟢 Enabled | | 🟢 Enabled | https://adguardteam.github.io/HostlistsRegistry/assets/filter_1.txt | 
| AdAway Default Blocklist | 🟢 Enabled | https://adguardteam.github.io/HostlistsRegistry/assets/filter_2.txt |  
| Stalkerware Indicators List | 🟢 Enabled | https://adguardteam.github.io/HostlistsRegistry/assets/filter_31.txt | 
| AdGuard DNS Popup Hosts filter | 🟢 Enabled | https://adguardteam.github.io/HostlistsRegistry/assets/filter_59.txt | 
| Dan Pollock's List | 🟢 Enabled | https://adguardteam.github.io/HostlistsRegistry/assets/filter_4.txt |  
| AWAvenue Ads Rule | 🟢 Enabled | https://adguardteam.github.io/HostlistsRegistry/assets/filter_53.txt | 
| HaGeZi's Ultimate Blocklist | 🟢 Enabled | https://adguardteam.github.io/HostlistsRegistry/assets/filter_49.txt | 
| OISD Blocklist Big | 🟢 Enabled | https://adguardteam.github.io/HostlistsRegistry/assets/filter_27.txt | 
| Peter Lowe's Blocklist | 🟢 Enabled | https://adguardteam.github.io/HostlistsRegistry/assets/filter_3.txt | 
| Steven Black's List | 🟢 Enabled | https://adguardteam.github.io/HostlistsRegistry/assets/filter_33.txt |  
| HaGeZi's Allowlist Referral | 🟢 Enabled | https://adguardteam.github.io/HostlistsRegistry/assets/filter_45.txt | 
| Dandelion Sprout Anti Push Notifications | 🟢 Enabled | https://adguardteam.github.io/HostlistsRegistry/assets/filter_39.txt | 
| Malicious URL Blocklist (URLHaus) | 🟢 Enabled | https://adguardteam.github.io/HostlistsRegistry/assets/filter_11.txt | 
| ShadowWhisperer's Dating List | 🟢 Enabled | https://adguardteam.github.io/HostlistsRegistry/assets/filter_57.txt | 
| NoCoin Filter List | 🟢 Enabled | https://adguardteam.github.io/HostlistsRegistry/assets/filter_8.txt |  
| Phishing Army | 🟢 Enabled | https://adguardteam.github.io/HostlistsRegistry/assets/filter_18.txt |  
| Phishing URL Blocklist (PhishTank and OpenPhish) | 🟢 Enabled | https://adguardteam.github.io/HostlistsRegistry/assets/filter_30.txt | 
| HaGeZi's The World's Most Abused TLDs | 🟢 Enabled | https://adguardteam.github.io/HostlistsRegistry/assets/filter_56.txt | 
| HaGeZi's Threat Intelligence Feeds (TIF) | 🟢 Enabled | https://adguardteam.github.io/HostlistsRegistry/assets/filter_44.txt | 
| Dandelion Sprout's Anti-Malware List | 🟢 Enabled | https://adguardteam.github.io/HostlistsRegistry/assets/filter_12.txt | 
| HaGeZi's DynDNS Blocklist | 🟢 Enabled | https://adguardteam.github.io/HostlistsRegistry/assets/filter_54.txt | 
| HaGeZi's Encrypted DNS/VPN/TOR/Proxy Bypass | 🟢 Enabled | https://adguardteam.github.io/HostlistsRegistry/assets/filter_52.txt | 
| The Blocklist Project Ads | 🟢 Enabled | https://blocklistproject.github.io/Lists/adguard/ads-ags.txt | 
| The Blocklist Project Tracking | 🟢 Enabled | https://blocklistproject.github.io/Lists/adguard/tracking-ags.txt | 
| The Blocklist Project Porn | 🟢 Enabled | https://blocklistproject.github.io/Lists/adguard/porn-ags.txt | 
| HaGeZi's Popup Ads | 🟢 Enabled | https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/adblock/popupads.txt | 
| ph00lt0 Blocklist Unified | 🟢 Enabled | https://raw.githubusercontent.com/ph00lt0/blocklists/master/blocklist.txt | 
| 1Hosts Pro | 🟢 Enabled | https://cdn.jsdelivr.net/gh/badmojr/1Hosts@master/Pro/adblock.txt | 
| EasyList AdServers | 🟢 Enabled | https://github.com/easylist/easylist/raw/master/easylist/easylist_adservers.txt | 
| EasyList Allowlist | 🟢 Enabled | https://github.com/easylist/easylist/raw/master/easylist/easylist_allowlist.txt | 
| EasyList Third Party | 🟢 Enabled | https://github.com/easylist/easylist/raw/master/easylist/easylist_thirdparty.txt | 
| EasyPrivacy Tracking Servers | 🟢 Enabled | https://github.com/easylist/easylist/raw/master/easyprivacy/easyprivacy_trackingservers.txt | 
| EasyPrivacy Tracking Servers Third Party | 🟢 Enabled | https://github.com/easylist/easylist/raw/master/easyprivacy/easyprivacy_trackingservers_thirdparty.txt | 
| EasyPrivacy Tracking Servers Notifications | 🟢 Enabled | https://github.com/easylist/easylist/raw/master/easyprivacy/easyprivacy_trackingservers_notifications.txt | 
| EasyPrivacy Tracking Servers Mining | 🟢 Enabled | https://github.com/easylist/easylist/raw/master/easyprivacy/easyprivacy_trackingservers_mining.txt | 
| EasyPrivacy Tracking Servers International | 🟢 Enabled | https://github.com/easylist/easylist/raw/master/easyprivacy/easyprivacy_trackingservers_international.txt | 
| EasyPrivacy Tracking Servers General | 🟢 Enabled | https://github.com/easylist/easylist/raw/master/easyprivacy/easyprivacy_trackingservers_general.txt |

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
