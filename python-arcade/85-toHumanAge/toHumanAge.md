<p>After years of practicing psychology you decided that it's time to find the answer to the following very important question: how can different species live together in harmony? In order to answer this question, you headed out for a long journey. After several years of wandering, you finally found what you were looking for: a village where humans, cats and dogs lived in the perfect harmony.</p>
<p>Trying to understand the source of this harmony, you are gathering information about all <code>members</code> of the village community. You're currently working on determining the age of each member converted to human age. Here's how cats and dogs age can be converted:</p>
<ul>
<li>The first and the second years of a cat's life are roughly equal to <code>12.5</code> years of a human's, and after this, each additional year is around four 'human years'.</li>
<li>The first year of a dog's life is equal to <code>15</code> years of a human's life, the second dog's year is equal to another <code>9</code> years of a human's life, and after this, each additional year is around four 'human years'.</li>
</ul>
<p>Given information about the <code>members</code> of the village community, return information about their ages converted to human age.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>members = [["cat", "2"], ["dog", "2"], ["human", "2"]]</code>,<br />
the output should be</p>
<pre><code>solution(members) = ["25 y.o. in human age", 
                       "24 y.o. in human age", 
                       "2 y.o. in human age"]
</code></pre>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.array.string members</strong></p>
<p>A list representing the members of the village community. Each member is given in the format <code>[<em>type</em>, <em>age</em>]</code>, where <code>type</code> can be <code>"cat"</code>, <code>"dog"</code> or <code>"human"</code>, and <code>age</code> is an integer in range <code>[0, 20]</code>.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ members.length ≤ 50</code>,<br />
<code>members[i].length = 2</code>,<br />
<code>members[i][0] ∈ {"cat", "dog", "human"}</code>,<br />
<code>0 ≤ int(members[i][1]) ≤ 20</code>.</p>
</li>
<li>
<p><strong>[output] array.string</strong></p>
<p>Information about each member (in the same order as they go in <code>members</code>) in the format <code><em>&lt;age&gt;</em> y.o. in human age</code>.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
