<p>You are organizing a team of eSportsmen, and you are determined to make it cool. You are already thinking about winning the world championship: when it happens, the names of your teammates will be chanted one after another by a large audience. You believe that it will sound cool if and only if the first letter of one player's name will be the same as the last letter in the name of the player before them.</p>
<p>Now you are considering one particular <code>team</code>. Its members are definitely professional gamers, but you're not sure if all together they form a cool team. Implement a function that will check if the <code>team</code> is cool.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>team = ["Mark", "Kelly", "Kurt", "Terk"]</code>, the output should be<br />
<code>solution(team) = true</code>.</p>
<p>The following team announcement will sound cool: <code>"Mark", "Kurt", "Terk", "Kelly"</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.string team</strong></p>
<p>A list of team members, where each team member is given by their name (a string consisting of English characters). Note that there are no names which start and end on the same letter.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ team.length ≤ 100</code>,<br />
<code>2 ≤ team[i].length ≤ 20</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if the team is cool, <code>false</code> otherwise.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
