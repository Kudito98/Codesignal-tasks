<p>A <code>step(x)</code> operation works like this: it changes a number <code>x</code> into <code>x - s(x)</code>, where <code>s(x)</code> is the sum of <code>x</code>'s digits. You like applying functions to numbers, so given the number <code>n</code>, you decide to build a decreasing sequence of numbers: <code>n</code>, <code>step(n)</code>, <code>step(step(n))</code>, etc., with <code>0</code> as the last element.</p>
<p>Building a single sequence isn't enough for you, so you replace all elements of the sequence with the sums of their digits (<code>s(x)</code>). Now you're curious as to which number appears in the new sequence most often. If there are several answers, return the maximal one.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>n = 88</code>, the output should be<br />
<code>solution(n) = 9</code>.</p>
<ul>
<li>Here is the first sequence you built: <code>88</code>, <code>72</code>, <code>63</code>, <code>54</code>, <code>45</code>, <code>36</code>, <code>27</code>, <code>18</code>, <code>9</code>, <code>0</code>;</li>
<li>And here is <code>s(x)</code> for each of its elements: <code>16</code>, <code>9</code>, <code>9</code>, <code>9</code>, <code>9</code>, <code>9</code>, <code>9</code>, <code>9</code>, <code>9</code>, <code>0</code>.</li>
</ul>
<p>As you can see, the most frequent number in the second sequence is <code>9</code>.</p>
</li>
<li>
<p>For <code>n = 8</code>, the output should be<br />
<code>solution(n) = 8</code>.</p>
<ul>
<li>At first you built the following sequence: <code>8</code>, <code>0</code></li>
<li><code>s(x)</code> for each of its elements is: <code>8</code>, <code>0</code></li>
</ul>
<p>As you can see, the answer is <code>8</code> (it appears as often as <code>0</code>, but is greater than it).</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer n</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ n ≤ 10<sup>5</sup></code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The most frequent number in the sequence <code>s(n)</code>, <code>s(step(n))</code>, <code>s(step(step(n)))</code>, etc.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
