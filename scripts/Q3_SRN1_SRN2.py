import numpy as np

def gram_schmidt(basis):
    """Converts basis vectors into orthonormal basis"""
    ortho_basis = []
    for v in basis:
        w = v.copy().astype(float)
        for u in ortho_basis:
            w -= np.dot(u, v) * u
        norm = np.linalg.norm(w)
        if norm > 1e-10:
            ortho_basis.append(w / norm)
    return ortho_basis

def project_onto_subspace(basis, signal):
    """Projects signal onto subspace spanned by basis"""
    ortho_basis = gram_schmidt(basis)
    projection = np.zeros_like(signal, dtype=float)
    for u in ortho_basis:
        projection += np.dot(signal, u) * u
    return projection

def main():
    n, k = map(int, input().split())
    
    basis = []
    for _ in range(k):
        vec = np.array(list(map(float, input().split())))
        basis.append(vec)
    
    signal = np.array(list(map(float, input().split())))
    
    projection = project_onto_subspace(basis, signal)
    print(' '.join([f"{x:.6f}" for x in projection]))

if __name__ == "__main__":
    main()