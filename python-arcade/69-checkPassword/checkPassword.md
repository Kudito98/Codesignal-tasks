<p>You're implementing a web application. Like most applications, yours also has the authorization function. Now you need to implement a server function that will check password attempts made by users. Since you expect heavy loads, the function should be able to accept a bunch of requests that will be sent simultaneously.</p>
<p>In order to validate your function, you want to test it locally. Given a list of <code>attempts</code> and the correct <code>password</code>, return the 1-based index of the first correct attempt, or <code>-1</code> if there were none.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>attempts = ["hello", "world", "I", "like", "coding"]</code> and<br />
<code>password = "like"</code>, the output should be<br />
<code>solution(attempts, password) = 4</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.string attempts</strong></p>
<p>A list of password attempts.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ attempts.length ≤ 20</code>,<br />
<code>1 ≤ attempts[i].length ≤ 20</code>.</p>
</li>
<li>
<p><strong>[input] string password</strong></p>
<p>Correct password.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ password.length ≤ 20</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The 1-based index of the first correct password attempt, or <code>-1</code> or there were none.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
