<p>The Abanamama Version System (AVS) is a software versioning and revision control system used in highly secure environments. In this system, each commit is assigned a unique name, the first part of which consists of the username encrypted in the base-4 system using symbols <code>'0'</code>, <code>'?'</code>, <code>'+'</code>, and <code>'!'</code>, and the second part consists of symbols of English alphabet.</p>
<p>Given such <code>commit</code>, your task is go remove the username part from it and return the second part as an answer.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>commit = "0??+0+!!someCommIdhsSt"</code>, the output should be<br />
<code>solution(commit) = "someCommIdhsSt"</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string commit</strong></p>
<p>Commit in the format given above. Note, that it is possible that it doesn't contain the first or the second part.</p>
<p><em>Guaranteed constraints:</em><br />
<code>5 ≤ commit.length ≤ 45</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p>The second part of the <code>commit</code>.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
