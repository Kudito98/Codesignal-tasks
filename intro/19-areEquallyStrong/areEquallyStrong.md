<p>Call two arms <em>equally strong</em> if the heaviest weights they each are able to lift are equal.</p>
<p>Call two people <em>equally strong</em> if their strongest arms are equally strong (the strongest arm can be both the right and the left), and so are their weakest arms.</p>
<p>Given your and your friend's arms' lifting capabilities find out if you two are equally strong.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>For <code>yourLeft = 10</code>, <code>yourRight = 15</code>, <code>friendsLeft = 15</code>, and <code>friendsRight = 10</code>, the output should be<br />
<code>solution(yourLeft, yourRight, friendsLeft, friendsRight) = true</code>;</li>
<li>For <code>yourLeft = 15</code>, <code>yourRight = 10</code>, <code>friendsLeft = 15</code>, and <code>friendsRight = 10</code>, the output should be<br />
<code>solution(yourLeft, yourRight, friendsLeft, friendsRight) = true</code>;</li>
<li>For <code>yourLeft = 15</code>, <code>yourRight = 10</code>, <code>friendsLeft = 15</code>, and <code>friendsRight = 9</code>, the output should be<br />
<code>solution(yourLeft, yourRight, friendsLeft, friendsRight) = false</code>.</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer yourLeft</strong></p>
<p>A non-negative integer representing the heaviest weight you can lift with your left arm.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ yourLeft ≤ 20</code>.</p>
</li>
<li>
<p><strong>[input] integer yourRight</strong></p>
<p>A non-negative integer representing the heaviest weight you can lift with your right arm.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ yourRight ≤ 20</code>.</p>
</li>
<li>
<p><strong>[input] integer friendsLeft</strong></p>
<p>A non-negative integer representing the heaviest weight your friend can lift with his or her left arm.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ friendsLeft ≤ 20</code>.</p>
</li>
<li>
<p><strong>[input] integer friendsRight</strong></p>
<p>A non-negative integer representing the heaviest weight your friend can lift with his or her right arm.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ friendsRight ≤ 20</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if you and your friend are equally strong, <code>false</code> otherwise.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
