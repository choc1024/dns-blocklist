# CHANGELOG
 
 
## v4.0
 
Time of Compilation: 2024-09-02 12:11:03.169707
Time Elapsed: 0:32:46.949097
 
Added my own allowlist that unblocks phishing.army that provides the phishing blocklist,\n removed EasyList Allowlist and HaGeZis Allowlist. I guess it is better to have false-positives than to have ad, malware and tracking domains reach us.
 
 
 
## Snapshot 2024-09-02 10:01:46.779685
 
Time of Compilation: 2024-09-02 10:01:46.779685
Time Elapsed: 0:31:55.907405
 
No changelog information provided
 
 
 
## v3.7
 
Time of Compilation: 2024-08-31 15:37:14.486180
Time Elapsed: 0:36:17.022659
 
Updated autoCompile.py script
 


## v3.5

OK, removing HaGeZi's Allowlist was a BAD idea... 
So um... I am adding it back. This is embarassing, but still, I realised that removing the allowlist actually breaks a lot of things, so I am going to add it back in this version.

Also, the last snapshot got kinda corrupted... maybe? Because the scirpt crashed as the gitlab credentials were out of date. So that's another reason for releasing this.

ALSO, added the HaGeZi's Pop-Up Ads filter.

## v3.0

Hey!
This build has been compiled with a new Python script, and from now on, most if not all builds will be compiled by it, so I don't have to do anything manually. Also, I think this will make building everything a lot easier, as the script will also automatically do git push.

## v2.3

Build Time: 13:39:41

In this build, the HaGeZi's Allowlist Referal has been removed. This may mean that email referals and others can stop working. If you need to unbeak them, you can always add the allowlist manually.

## v2.0

Build Start: 13/8/2024 15:02:27
Built Time: 1:01:56

In this build, most things are the same, except that starting from this build, all URLs are from the original sources whenever possible instead of AdGuard Home, and this has been done to improve liability and possibly more up-to-date blocklists.

## v1.0

Build Start: 8/5/2024 15:40:18

This is the first build, included lists can be found in the config.json. Transformations are: ["Deduplicate", "Compress", "RemoveEmptyLines", "TrimLines", "InsertFinalNewLine"] or can also be checked in the config.json. Most URLs are hosted by the AdGuard Home Team on their GitHub Page.
