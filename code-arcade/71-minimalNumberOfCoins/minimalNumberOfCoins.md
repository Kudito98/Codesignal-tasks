<p>You find yourself in Bananaland trying to buy a banana. You are super rich so you have an unlimited supply of banana-coins, but you are trying to use as few coins as possible.</p>
<p>The coin values available in Bananaland are stored in a sorted array <code>coins</code>. <code>coins[0] = 1</code>, and for each <code>i (0 &lt; i &lt; coins.length)</code> <code>coins[i]</code> is divisible by <code>coins[i - 1]</code>. Find the minimal number of banana-coins you'll have to spend to buy a banana given the banana's <code>price</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>coins = [1, 2, 10]</code> and <code>price = 28</code>, the output should be<br />
<code>solution(coins, price) = 6</code>.</p>
<p>You have to use <code>10</code> twice, and <code>2</code> four times.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.integer coins</strong></p>
<p>The coin values available in Bananaland.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ coins.length ≤ 5</code>,<br />
<code>1 ≤ coins[i] ≤ 120</code>.</p>
</li>
<li>
<p><strong>[input] integer price</strong></p>
<p>A positive integer representing the price of the banana.</p>
<p><em>Guaranteed constraints:</em><br />
<code>8 ≤ price ≤ 250</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The minimal number of coins you can use to buy the banana.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
