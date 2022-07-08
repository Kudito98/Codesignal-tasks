<p>You are playing an RPG game. Currently your experience points (XP) total is equal to <code>experience</code>. To reach the next level your XP should be at least at <code>threshold</code>. If you kill the monster in front of you, you will gain more experience points in the amount of the <code>reward</code>.</p>
<p>Given values <code>experience</code>, <code>threshold</code> and <code>reward</code>, check if you reach the next level after killing the monster.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>For <code>experience = 10</code>, <code>threshold = 15</code>, and <code>reward = 5</code>, the output should be<br />
<code>solution(experience, threshold, reward) = true</code>;</li>
<li>For <code>experience = 10</code>, <code>threshold = 15</code>, and <code>reward = 4</code>, the output should be<br />
<code>solution(experience, threshold, reward) = false</code>.</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer experience</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>3 ≤ experience ≤ 250</code>.</p>
</li>
<li>
<p><strong>[input] integer threshold</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>5 ≤ threshold ≤ 300</code>.</p>
</li>
<li>
<p><strong>[input] integer reward</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>2 ≤ reward ≤ 65</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if you reach the next level, <code>false</code> otherwise.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
