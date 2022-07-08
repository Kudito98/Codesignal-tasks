<p>The web application service you're working on is supposed to be used by developers teams. To make the service more friendly, you'd like to implement a feature that will greet each person in a group.</p>
<p>Given a list of people in a <code>team</code>, return an array of greetings that should be printed out, where each greeting is in the format <code>"Hello, <em>&lt;team[i]&gt;</em>!"</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>team = ["Athos", "Porthos", "Aramis"]</code>,<br />
the output should be</p>
<pre><code>solution(team) = ["Hello, Athos!",
                            "Hello, Porthos!",
                            "Hello, Aramis!"]
</code></pre>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.string team</strong></p>
<p>A list of team members.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ team.length ≤ 10</code>,<br />
<code>1 ≤ team[i].length ≤ 10</code>.</p>
</li>
<li>
<p><strong>[output] array.string</strong></p>
<p>Array of strings, where the <code>i<sup>th</sup></code> string has the format <code>"Hello, <em>&lt;team[i]&gt;</em>!"</code>.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
