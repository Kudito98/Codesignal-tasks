<p>In a large and famous supermarket a new major campaign was launched. From now on, each <code>n<sup>th</sup></code> customer has a chance to win a prize: a brand new luxury car! However, it's not that simple. A customer wins a prize only if the total price of their purchase is divisible by <code>d</code>. This number is kept as a secret, so the customers don't know in advance how much they should spend on their purchases. The winners will be announced once the campaign is over.</p>
<p>Your task is to implement a function that will determine the winners. Given the <code>purchases</code> of some customers over time, return the 1-based indices of all the customers who won the prize, i.e. each <code>n<sup>th</sup></code> who spend on their purchases amount of money divisible by <code>d</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>purchases = [12, 43, 13, 465, 1, 13]</code>, <code>n = 2</code>, and <code>d = 3</code>,<br />
the output should be<br />
<code>solution(purchases, n, d) = [4]</code>.</p>
<p>Each second customer has a chance to win a car, which makes customers <code>2</code>, <code>4</code> and <code>6</code> potential winners. Customer number <code>2</code> spent <code>43</code> on his purchase, which is not divisible by <code>3</code>. <code>13</code> also is not divisible by <code>3</code>, so the sixth customer also doesn't get the price. Customer <code>4</code>, however, spent <code>465</code>, which is divisible by <code>3</code>, so he is the only lucky guy.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.integer purchases</strong></p>
<p>A list that represents the cost of the purchases some customers made.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ purchases.length ≤ 100</code>,<br />
<code>1 ≤ purchases[i] ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[input] integer n</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>2 ≤ n ≤ 20</code>.</p>
</li>
<li>
<p><strong>[input] integer d</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>2 ≤ d ≤ 20</code>.</p>
</li>
<li>
<p><strong>[output] array.integer</strong></p>
<p>A sorted list of 1-based customers who won the prize.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
