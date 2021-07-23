Sometimes, you may have xml files with duplicated lines.
For example, 


<e:resource id="1234" uuid="UUID-abcd-efgh-f1e5a439" type="text" subtype="">
<e:content lang="en" progress="0" fuzzy="0" progress-ctime="0" words="1">First line of text at paligo
</e:content>
</e:resource>
<e:resource id="4567" uuid="UUID-jklmn-0pqrs-5d5cb1cc" type="text" subtype="">
<e:content lang="en" progress="0" fuzzy="0" progress-ctime="0" words="4">Second line line of text at paligo
</e:content>
</e:resource>
#This line is repeated with same text but different id. Ideally, it should have the same id for paligo to make reused text
<e:resource id="7891" uuid="UUID-abcd-efgh-f1e5a439" type="text" subtype="">
<e:content lang="en" progress="0" fuzzy="0" progress-ctime="0" words="1">First line of text at paligo
</e:content>
</e:resource>

With this script, you can run through xml file to find similar texts, with different ids to convert it to paligo reused text

