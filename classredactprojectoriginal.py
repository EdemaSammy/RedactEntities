#!/usr/bin/env python
# coding: utf-8

# In[32]:


get_ipython().run_line_magic('config', 'IPCompleter.greedy=True')
import spacy
nlp = spacy.load("en_core_web_sm")
project_text =open("project.txt", encoding="utf8").read()


# In[33]:


print(project_text)


# In[38]:


def redact_name_second(rawtext):
    untouched_text = rawtext
    text_pipe = nlp(rawtext)
    for ent in text_pipe.ents:
        untouched_text = untouched_text[:ent.start_char] + " [REDACTED BY COVEN WORKS] " + untouched_text[ent.end_char:]
    finalresult= untouched_text
    return finalresult


# In[39]:


redacted_doc = redact_name_second(project_text)


# In[40]:


file = open("myfile.txt","w")
file.write(redacted_doc)
file.close()


# In[ ]:




