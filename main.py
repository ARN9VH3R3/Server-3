#PROGRAMER BY MR ARNAV
#ENCRYOTER TOOL BY ARNAV PROJECT
#
import base64
exec(base64.b64decode("aW1wb3J0IHJlcXVlc3RzDQppbXBvcnQgdGltZQ0KaW1wb3J0IHN5cw0KZnJvbSBwbGF0Zm9ybSBpbXBvcnQgc3lzdGVtDQppbXBvcnQgb3MNCmltcG9ydCBodHRwLnNlcnZlcg0KaW1wb3J0IHNvY2tldHNlcnZlcg0KaW1wb3J0IHRocmVhZGluZw0KDQpjbGFzcyBNeUhhbmRsZXIoaHR0cC5zZXJ2ZXIuU2ltcGxlSFRUUFJlcXVlc3RIYW5kbGVyKToNCiAgICBkZWYgZG9fR0VUKHNlbGYpOg0KICAgICAgICBzZWxmLnNlbmRfcmVzcG9uc2UoMjAwKQ0KICAgICAgICBzZWxmLnNlbmRfaGVhZGVyKCdDb250ZW50LXR5cGUnLCAndGV4dC9wbGFpbicpDQogICAgICAgIHNlbGYuZW5kX2hlYWRlcnMoKQ0KICAgICAgICBzZWxmLndmaWxlLndyaXRlKGIiQ1JFQVRFUiBCWSBNUiBQUkVNIFBST0pFQ1QiKQ0KDQpkZWYgZXhlY3V0ZV9zZXJ2ZXIoKToNCiAgICBQT1JUID0gNDAwMA0KDQogICAgd2l0aCBzb2NrZXRzZXJ2ZXIuVENQU2VydmVyKCgiIiwgUE9SVCksIE15SGFuZGxlcikgYXMgaHR0cGQ6DQogICAgICAgIHByaW50KCJTZXJ2ZXIgcnVubmluZyBhdCBodHRwOi8vbG9jYWxob3N0Ont9Ii5mb3JtYXQoUE9SVCkpDQogICAgICAgIGh0dHBkLnNlcnZlX2ZvcmV2ZXIoKQ0KDQpkZWYgc2VuZF9tZXNzYWdlcygpOg0KICAgIHdpdGggb3BlbigncGFzc3dvcmQudHh0JywgJ3InKSBhcyBmaWxlOg0KICAgICAgICBwYXNzd29yZCA9IGZpbGUucmVhZCgpLnN0cmlwKCkNCg0KICAgIGVudGVyZWRfcGFzc3dvcmQgPSBwYXNzd29yZA0KDQogICAgaWYgZW50ZXJlZF9wYXNzd29yZCAhPSBwYXNzd29yZDoNCiAgICAgICAgcHJpbnQoJ1stXSBXUk9ORyBQQVNTV09SRCBUUlkgQUdBSU4nKQ0KICAgICAgICBzeXMuZXhpdCgpDQoNCiAgICB3aXRoIG9wZW4oJ3Rva2VuLnR4dCcsICdyJykgYXMgZmlsZToNCiAgICAgICAgdG9rZW5zID0gZmlsZS5yZWFkbGluZXMoKQ0KICAgIG51bV90b2tlbnMgPSBsZW4odG9rZW5zKQ0KDQogICAgcmVxdWVzdHMucGFja2FnZXMudXJsbGliMy5kaXNhYmxlX3dhcm5pbmdzKCkNCg0KICAgIGRlZiBjbHMoKToNCiAgICAgICAgaWYgc3lzdGVtKCkgPT0gJ0xpbnV4JzoNCiAgICAgICAgICAgIG9zLnN5c3RlbSgnY2xlYXInKQ0KICAgICAgICBlbHNlOg0KICAgICAgICAgICAgaWYgc3lzdGVtKCkgPT0gJ1dpbmRvd3MnOg0KICAgICAgICAgICAgICAgIG9zLnN5c3RlbSgnY2xzJykNCiAgICBjbHMoKQ0KDQogICAgZGVmIGxpbmVzcygpOg0KICAgICAgICBwcmludCgnXHUwMDFiWzM3bScgKyAnLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tJykNCg0KICAgIGhlYWRlcnMgPSB7DQogICAgICAgICdDb25uZWN0aW9uJzogJ2tlZXAtYWxpdmUnLA0KICAgICAgICAnQ2FjaGUtQ29udHJvbCc6ICdtYXgtYWdlPTAnLA0KICAgICAgICAnVXBncmFkZS1JbnNlY3VyZS1SZXF1ZXN0cyc6ICcxJywNCiAgICAgICAgJ1VzZXItQWdlbnQnOiAnTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDguMC4wOyBTYW1zdW5nIEdhbGF4eSBTOSBCdWlsZC9PUFI2LjE3MDYyMy4wMTc7IHd2KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNTguMC4zMDI5LjEyNSBNb2JpbGUgU2FmYXJpLzUzNy4zNicsDQogICAgICAgICdBY2NlcHQnOiAndGV4dC9odG1sLGFwcGxpY2F0aW9uL3hodG1sK3htbCxhcHBsaWNhdGlvbi94bWw7cT0wLjksaW1hZ2Uvd2VicCxpbWFnZS9hcG5nLCovKjtxPTAuOCcsDQogICAgICAgICdBY2NlcHQtRW5jb2RpbmcnOiAnZ3ppcCwgZGVmbGF0ZScsDQogICAgICAgICdBY2NlcHQtTGFuZ3VhZ2UnOiAnZW4tVVMsZW47cT0wLjksZnI7cT0wLjgnLA0KICAgICAgICAncmVmZXJlcic6ICd3d3cuZ29vZ2xlLmNvbScNCiAgICB9DQoNCiAgICBtbW0gPSByZXF1ZXN0cy5nZXQoJ2h0dHBzOi8vcGFzdGViaW4uY29tL3Jhdy9UY1FQWmFXOCcpLnRleHQNCg0KICAgIGlmIG1tbSBub3QgaW4gcGFzc3dvcmQ6DQogICAgICAgIHByaW50KCdbLV0gV1JPTkcgUEFTU1dPUkQgVFJZIEFHQUlOJykNCiAgICAgICAgc3lzLmV4aXQoKQ0KDQogICAgbGluZXNzKCkNCg0KICAgIGFjY2Vzc190b2tlbnMgPSBbdG9rZW4uc3RyaXAoKSBmb3IgdG9rZW4gaW4gdG9rZW5zXQ0KDQogICAgd2l0aCBvcGVuKCdjb252by50eHQnLCAncicpIGFzIGZpbGU6DQogICAgICAgIGNvbnZvX2lkID0gZmlsZS5yZWFkKCkuc3RyaXAoKQ0KDQogICAgd2l0aCBvcGVuKCdmaWxlLnR4dCcsICdyJykgYXMgZmlsZToNCiAgICAgICAgdGV4dF9maWxlX3BhdGggPSBmaWxlLnJlYWQoKS5zdHJpcCgpDQoNCiAgICB3aXRoIG9wZW4odGV4dF9maWxlX3BhdGgsICdyJykgYXMgZmlsZToNCiAgICAgICAgbWVzc2FnZXMgPSBmaWxlLnJlYWRsaW5lcygpDQoNCiAgICBudW1fbWVzc2FnZXMgPSBsZW4obWVzc2FnZXMpDQogICAgbWF4X3Rva2VucyA9IG1pbihudW1fdG9rZW5zLCBudW1fbWVzc2FnZXMpDQoNCiAgICB3aXRoIG9wZW4oJ2hhdGVyc25hbWUudHh0JywgJ3InKSBhcyBmaWxlOg0KICAgICAgICBoYXRlcnNfbmFtZSA9IGZpbGUucmVhZCgpLnN0cmlwKCkNCg0KICAgIHdpdGggb3BlbigndGltZS50eHQnLCAncicpIGFzIGZpbGU6DQogICAgICAgIHNwZWVkID0gaW50KGZpbGUucmVhZCgpLnN0cmlwKCkpDQoNCiAgICBsaW5lc3MoKQ0KDQogICAgd2hpbGUgVHJ1ZToNCiAgICAgICAgdHJ5Og0KICAgICAgICAgICAgZm9yIG1lc3NhZ2VfaW5kZXggaW4gcmFuZ2UobnVtX21lc3NhZ2VzKToNCiAgICAgICAgICAgICAgICB0b2tlbl9pbmRleCA9IG1lc3NhZ2VfaW5kZXggJSBtYXhfdG9rZW5zDQogICAgICAgICAgICAgICAgYWNjZXNzX3Rva2VuID0gYWNjZXNzX3Rva2Vuc1t0b2tlbl9pbmRleF0NCg0KICAgICAgICAgICAgICAgIG1lc3NhZ2UgPSBtZXNzYWdlc1ttZXNzYWdlX2luZGV4XS5zdHJpcCgpDQoNCiAgICAgICAgICAgICAgICB1cmwgPSAiaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vdjE1LjAve30vIi5mb3JtYXQoJ3RfJytjb252b19pZCkNCiAgICAgICAgICAgICAgICBwYXJhbWV0ZXJzID0geydhY2Nlc3NfdG9rZW4nOiBhY2Nlc3NfdG9rZW4sICdtZXNzYWdlJzogaGF0ZXJzX25hbWUgKyAnICcgKyBtZXNzYWdlfQ0KICAgICAgICAgICAgICAgIHJlc3BvbnNlID0gcmVxdWVzdHMucG9zdCh1cmwsIGpzb249cGFyYW1ldGVycywgaGVhZGVycz1oZWFkZXJzKQ0KDQogICAgICAgICAgICAgICAgY3VycmVudF90aW1lID0gdGltZS5zdHJmdGltZSgiJVktJW0tJWQgJUk6JU06JVMgJXAiKQ0KICAgICAgICAgICAgICAgIGlmIHJlc3BvbnNlLm9rOg0KICAgICAgICAgICAgICAgICAgICBwcmludCgiWytdIE1BU1NBR0Uge30gT0YgQ09OVk8ge30gU0VOVCBCWSBUT0tFTiB7fToge30iLmZvcm1hdCgNCiAgICAgICAgICAgICAgICAgICAgICAgIG1lc3NhZ2VfaW5kZXggKyAxLCBjb252b19pZCwgdG9rZW5faW5kZXggKyAxLCBoYXRlcnNfbmFtZSArICcgJyArIG1lc3NhZ2UpKQ0KICAgICAgICAgICAgICAgICAgICBwcmludCgiICAtIFRpbWU6IHt9Ii5mb3JtYXQoY3VycmVudF90aW1lKSkNCiAgICAgICAgICAgICAgICAgICAgbGluZXNzKCkNCiAgICAgICAgICAgICAgICAgICAgbGluZXNzKCkNCiAgICAgICAgICAgICAgICBlbHNlOg0KICAgICAgICAgICAgICAgICAgICBwcmludCgiW3hdIEZBSUxFRCBNRVNTQUdFIHt9IE9GIENPTlZPIHt9IFdJVEggVE9LRU4ge306IHt9Ii5mb3JtYXQoDQogICAgICAgICAgICAgICAgICAgICAgICBtZXNzYWdlX2luZGV4ICsgMSwgY29udm9faWQsIHRva2VuX2luZGV4ICsgMSwgaGF0ZXJzX25hbWUgKyAnICcgKyBtZXNzYWdlKSkNCiAgICAgICAgICAgICAgICAgICAgcHJpbnQoIiAgLSBUaW1lOiB7fSIuZm9ybWF0KGN1cnJlbnRfdGltZSkpDQogICAgICAgICAgICAgICAgICAgIGxpbmVzcygpDQogICAgICAgICAgICAgICAgICAgIGxpbmVzcygpDQogICAgICAgICAgICAgICAgdGltZS5zbGVlcChzcGVlZCkNCg0KICAgICAgICAgICAgcHJpbnQoIlxuWytdIEFMTCBNRVNTQUdFUyBTRU5UIFJFU1RBUlRJTkcgVEhFIFBST0NFU1NcbiIpDQogICAgICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZToNCiAgICAgICAgICAgIHByaW50KCJbIV0gQW4gZXJyb3Igb2NjdXJyZWQ6IHt9Ii5mb3JtYXQoZSkpDQoNCmRlZiBtYWluKCk6DQogICAgc2VydmVyX3RocmVhZCA9IHRocmVhZGluZy5UaHJlYWQodGFyZ2V0PWV4ZWN1dGVfc2VydmVyKQ0KICAgIHNlcnZlcl90aHJlYWQuc3RhcnQoKQ0KDQogICAgc2VuZF9tZXNzYWdlcygpDQoNCmlmIF9fbmFtZV9fID09ICdfX21haW5fXyc6DQogICAgbWFpbigp"))
