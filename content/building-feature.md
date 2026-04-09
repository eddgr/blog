title: What To Do After You Build A Feature
slug: building-feature
date: 2020-11-04

On Writing Well by William Zizner was a mandatory book for my creative writing class in college and it's a book that I still reference in my life. One of the core principles for writing well (that applies to words and code) is to get rid of clutter to make it more impactful. How does this apply to coding?

Once you're done coding your feature, create a merge request and look at the changes you contributed. You can see the changes you made and as you review them, you should be able to see areas where you can refactor or abstract code out. Here are some questions you can ask yourself when going over your code:

- Is code being repeated? Can it be made into a helper function or component?
- Can this function be rewritten so that it's cleaner?
- Do I need to write a comment for my future self to describe the purpose of this section of code?

Use comments in the merge request to make notes for yourself and to create a todo list of issues to resolve.

Once that's done, you repeat the process again until no new comments are added. Only then will you be done with the feature.

