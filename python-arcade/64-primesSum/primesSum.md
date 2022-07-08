<p>It is believed by some tribes of South Codelenica that only two events determine the person's destiny: the first time he picked a flower, and the first time he planted one. They also believe in the power of <a href="keyword://prime-number" target="_blank">prime numbers</a> and in the power of sums (and a bunch of other most probably unrelated stuff), so you are wondering if it has something to do with their belief in the destiny-determining events.</p>
<p>You know that you first picked a flower in year <code>a</code> of the Codelenican calendar, and planted it in year <code>b</code>. Now you're curious about the sum of all the <em>prime</em> numbers in the range <code>[a, b]</code>, to see if this number could possibly affect your life.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>a = 10</code> and <code>b = 20</code>, the output should be<br />
<code>solution(a, b) = 60</code>.</p>
<p>There are <code>4</code> <em>prime</em> numbers in the range <code>[10, 20]</code>: <code>11</code>, <code>13</code>, <code>17</code> and <code>19</code>. Their sum is equal to <code>11 + 13 + 17 + 19 = 60</code>. It's a round number, maybe it does mean something?..</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer a</strong></p>
<p>The year in which you picked a flower for the first time.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ a ≤ b ≤ 10<sup>5</sup></code>.</p>
</li>
<li>
<p><strong>[input] integer b</strong></p>
<p>The year in which you planted a flower for the first time.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ a ≤ b ≤ 10<sup>5</sup></code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The sum of <em>prime</em> numbers in the range <code>[a, b]</code>.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
