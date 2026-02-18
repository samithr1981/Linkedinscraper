#!/usr/bin/env python
# coding: utf-8

# In[14]:


import sys
print(sys.executable)
import sys
get_ipython().system('{sys.executable} -m pip install playwright')
get_ipython().system('{sys.executable} -m playwright install chromium')


# In[15]:


from playwright.sync_api import sync_playwright
import json, time

def scrape_linkedin_feed(email, password):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=True after testing
        page = browser.new_page()
        
        # Login
        page.goto("which-website")
        page.fill("your-login-details", email)
        page.fill("your-password", password)
        page.click('[type="submit"]')
        page.wait_for_timeout(3000)
        
        # Go to feed
        page.goto("https://www.linkedin.com/feed/")
        
        posts = []
        # Scroll and collect posts
        for _ in range(10):  # adjust scroll count
            page.evaluate("window.scrollBy(0, 1000)")
            page.wait_for_timeout(2000)
        
        # Extract post text
        post_elements = page.query_selector_all(".feed-shared-update-v2")
        for el in post_elements:
            try:
                text = el.inner_text()
                posts.append(text[:1000])  # cap length
            except:
                pass
        
        browser.close()
        return posts


# In[16]:


import sys
get_ipython().system('{sys.executable} -m pip install anthropic')


# In[17]:


pip install groq


# In[20]:

#This is just to test before going into the website, this should work
from groq import Groq

client = Groq(api_key="your-api-key")  # get free key at console.groq.com

test_posts = [
    "GPT-5 was just announced with amazing new reasoning capabilities!",
    "Just had a great lunch at a new restaurant downtown.",
    "Anthropic released Claude 3.5 with major improvements in coding and analysis.",
    "Tips for better work-life balance in 2024."
]

combined = "\n\n---\n\n".join(test_posts)

prompt = f"""You are analyzing LinkedIn posts from the last 24 hours.
Posts:
{combined}
Please:

1. Give a concise summary of key themes and insights
2. For each relevant post, suggest a thoughtful comment I could leave
Format your response clearly with sections: Summary, Key Posts & Suggested Comments."""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": prompt}]
)

print(response.choices[0].message.content)


# In[22]:


import asyncio
from playwright.async_api import async_playwright
from groq import Groq

# ---- CONFIG ----
LINKEDIN_EMAIL = "your login id"
LINKEDIN_PASSWORD = "password"
GROQ_API_KEY = "your-api-key"

# ---- STEP 1: SCRAPE LINKEDIN FEED ----
async def scrape_linkedin_feed():
    posts = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # Login
        await page.goto("https://www.linkedin.com/login")
        await page.fill("#username", LINKEDIN_EMAIL)
        await page.fill("#password", LINKEDIN_PASSWORD)
        await page.click('[type="submit"]')
        await page.wait_for_timeout(5000)

        input("If 2FA appeared, complete it now then press ENTER to continue...")

        await page.goto("https://www.linkedin.com/feed/")
        await page.wait_for_timeout(3000)

        print("Scrolling feed...")
        for i in range(15):
            await page.evaluate("window.scrollBy(0, 800)")
            await page.wait_for_timeout(1500)

        post_elements = await page.query_selector_all(".feed-shared-update-v2")
        print(f"Found {len(post_elements)} posts")

        for el in post_elements:
            try:
                text = await el.inner_text()
                if len(text.strip()) > 50:
                    posts.append(text[:1500])
            except:
                pass

        await browser.close()
    return posts

# ---- STEP 2: ANALYZE WITH GROQ ----
def analyze_posts(posts):
    if not posts:
        print("No posts found!")
        return

    client = Groq(api_key=GROQ_API_KEY)
    combined = "\n\n---\n\n".join(posts)

    prompt = f"""You are analyzing LinkedIn posts scraped from a user's feed.

Posts:
{combined}

Please:
1. Filter only AI-related posts and ignore the rest
2. Give a concise summary of key AI themes and insights
3. For each AI-related post, suggest a thoughtful, professional comment

Format your response as:
## Summary
...

## AI-Related Posts & Suggested Comments
**Post:** (brief description)
**Suggested Comment:** ...
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# ---- RUN IT ----
print("Starting LinkedIn scraper...")
posts = await scrape_linkedin_feed()
print(f"Scraped {len(posts)} posts. Analyzing...")
result = analyze_posts(posts)
print("\n" + "="*60)
print(result)


# In[23]:


import asyncio
from playwright.async_api import async_playwright
from groq import Groq

# ---- CONFIG ----
LINKEDIN_EMAIL = "your login id"
LINKEDIN_PASSWORD = "your password"
GROQ_API_KEY = "your-api-key"

# ---- STEP 1: SCRAPE LINKEDIN FEED ----
async def scrape_linkedin_feed():
    posts = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # Login
        await page.goto("https://www.linkedin.com/login")
        await page.fill("#username", LINKEDIN_EMAIL)
        await page.fill("#password", LINKEDIN_PASSWORD)
        await page.click('[type="submit"]')
        await page.wait_for_timeout(5000)

        input("If 2FA appeared, complete it now then press ENTER to continue...")

        await page.goto("https://www.linkedin.com/feed/")
        await page.wait_for_timeout(3000)

        print("Scrolling feed...")
        for i in range(15):
            await page.evaluate("window.scrollBy(0, 800)")
            await page.wait_for_timeout(1500)

        post_elements = await page.query_selector_all(".feed-shared-update-v2")
        print(f"Found {len(post_elements)} posts")

        for el in post_elements:
            try:
                text = await el.inner_text()
                if len(text.strip()) > 50:
                    posts.append(text[:1500])
            except:
                pass

        await browser.close()
    return posts

# ---- STEP 2: ANALYZE WITH GROQ ----
def analyze_posts(posts):
    if not posts:
        print("No posts found!")
        return

    client = Groq(api_key=GROQ_API_KEY)
    combined = "\n\n---\n\n".join(posts)

    prompt = f"""You are analyzing LinkedIn posts scraped from a user's feed.

Posts:
{combined}

Please:
2. Give a concise summary of key AI themes and insights
3. For each AI-related post, suggest a thoughtful, professional comment

Format your response as:
## Summary
...

## AI-Related Posts & Suggested Comments
**Post:** (brief description)
**Suggested Comment:** ...
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# ---- RUN IT ----
print("Starting LinkedIn scraper...")
posts = await scrape_linkedin_feed()
print(f"Scraped {len(posts)} posts. Analyzing...")
result = analyze_posts(posts)
print("\n" + "="*60)
print(result)






