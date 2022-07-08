<p>The greatest ever Rock-Paper-Scissors Championship will take place in your town! The best <code>players</code> will battle each other to see who's the best player in the world. Each player will compete against each other player twice, once home and once away.</p>
<p>Given the list of the <code>players</code>, your task is to come up with the list of all the games between them, and return them sorted <a href="keyword://lexicographical-order-for-arrays" target="_blank">lexicographically</a>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>players = ["trainee", "warrior", "ninja"]</code>, the output should be</p>
<pre><code>solution(players) = [["ninja", "trainee"], ["ninja", "warrior"], 
                              ["trainee", "ninja"], ["trainee", "warrior"], 
                              ["warrior", "ninja"], ["warrior", "trainee"]]
</code></pre>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.string players</strong></p>
<p>A list of distinct players, where each player is given by their nickname that can consist of English letters and whitespace characters.</p>
<p><em>Guaranteed constraints:</em><br />
<code>2 ≤ players.length ≤ 10</code>,<br />
<code>1 ≤ players[i].length ≤ 50</code>.</p>
</li>
<li>
<p><strong>[output] array.array.string</strong></p>
<p>Array of pairs of players that will play against one another sorted <em>lexicographically</em>.</p>
<p><em>Note</em>: if your solution returns a list of tuples, the tuples will be converted to list automatically.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
