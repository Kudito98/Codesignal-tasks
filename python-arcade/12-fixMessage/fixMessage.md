<p>One of your friends has an awful writing style: he almost never starts a message with a capital letter, but adds uppercase letters in random places throughout the message. It makes chatting with him very difficult for you, so you decided to write a plugin that will change each <code>message</code> received from your friend into a more readable form.</p>
<p>Implement a function that will change the very first symbol of the given <code>message</code> to uppercase, and make all the other letters lowercase.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>message = "you'll NEVER believe what that 'FrIeNd' of mine did!!1"</code>,<br />
the output should be<br />
<code>solution(message) = "You'll never believe what that 'friend' of mine did!!1"</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string message</strong></p>
<p>A string consisting of English letters, whitespace characters, digits and punctuation marks.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ message.length ≤ 65</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p>Fixed <code>message</code> with its first letter capitalized, and all other letters converted to lowercase.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
