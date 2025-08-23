---
description: Comprehensive Rust guidelines optimized for AI agents developing Solana smart contracts. Includes Anchor framework patterns, security best practices, testing strategies, and performance optimization.
globs: /**/*.rs, programs/**/*.rs, src/**/*.rs, tests/**/*.rs
---

# Rust + Solana Development Guidelines for AI Agents

## 1. Program Architecture Standards

### Project Structure Requirements

**MANDATORY STRUCTURE:**

```text
my-solana-program/
├── Anchor.toml
├── programs/
│   └── my-program/
│       ├── Cargo.toml
│       └── src/
│           ├── lib.rs          # Program entrypoint
│           ├── instructions/   # Instruction handlers
│           ├── state/          # Account definitions
│           ├── error.rs        # Custom errors
│           └── utils.rs        # Helper functions
├── tests/
│   └── my-program.ts
└── target/
```

### Core Program Structure

```rust
// programs/my-program/src/lib.rs
use anchor_lang::prelude::*;

declare_id!("Fg6PaFpoGXkYsidMpWTK6W2BeZ7FEfcYkg476zPFsLnS");

pub mod instructions;
pub mod state;
pub mod error;

use instructions::*;
use error::*;

#[program]
pub mod my_program {
    use super::*;

    pub fn initialize(ctx: Context<Initialize>, name: String) -> Result<()> {
        instructions::initialize::handler(ctx, name)
    }

    pub fn update_user(ctx: Context<UpdateUser>, new_name: String) -> Result<()> {
        instructions::update::handler(ctx, new_name)
    }
}
```

### Instruction Module Pattern

```rust
// programs/my-program/src/instructions/initialize.rs
use anchor_lang::prelude::*;
use crate::state::User;
use crate::error::MyProgramError;

pub fn handler(ctx: Context<Initialize>, name: String) -> Result<()> {
    require!(!name.is_empty(), MyProgramError::InvalidName);
    require!(name.len() <= 50, MyProgramError::NameTooLong);
    
    let user = &mut ctx.accounts.user;
    user.authority = ctx.accounts.authority.key();
    user.name = name;
    user.created_at = Clock::get()?.unix_timestamp;
    user.bump = *ctx.bumps.get("user").unwrap();
    
    Ok(())
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(
        init,
        payer = authority,
        space = User::SIZE,
        seeds = [b"user", authority.key().as_ref()],
        bump
    )]
    pub user: Account<'info, User>,
    
    #[account(mut)]
    pub authority: Signer<'info>,
    
    pub system_program: Program<'info, System>,
}
```

## 2. State Management and Security

### Account State Definitions

```rust
// programs/my-program/src/state/user.rs
use anchor_lang::prelude::*;

#[account]
#[derive(Default)]
pub struct User {
    pub authority: Pubkey,   // 32 bytes
    pub name: String,        // 4 + 50 bytes
    pub created_at: i64,     // 8 bytes
    pub updated_at: i64,     // 8 bytes
    pub bump: u8,            // 1 byte
}

impl User {
    pub const SIZE: usize = 8 + 32 + 4 + 50 + 8 + 8 + 1;
    pub const MAX_NAME_LENGTH: usize = 50;
    
    pub fn validate(&self) -> Result<()> {
        require!(!self.name.is_empty(), crate::error::MyProgramError::InvalidName);
        require!(self.name.len() <= Self::MAX_NAME_LENGTH, crate::error::MyProgramError::NameTooLong);
        Ok(())
    }
}

// For large accounts, use zero-copy
#[account(zero_copy)]
#[repr(C)]
pub struct LargeData {
    pub data: [u64; 1000],
}
```

### Security Validation Patterns

```rust
// ✅ Good - Comprehensive account validation
#[derive(Accounts)]
pub struct SecureUpdate<'info> {
    #[account(
        mut,
        has_one = authority @ MyProgramError::Unauthorized,
        seeds = [b"user", authority.key().as_ref()],
        bump = user.bump
    )]
    pub user: Account<'info, User>,
    
    pub authority: Signer<'info>,
    
    #[account(address = system_program::ID)]
    pub system_program: Program<'info, System>,
}

// ✅ Good - Safe CPI calls
use anchor_spl::token::{self, Token, TokenAccount, Transfer};

pub fn secure_transfer(ctx: Context<SecureTransfer>, amount: u64) -> Result<()> {
    require!(
        ctx.accounts.token_program.key() == token::ID,
        MyProgramError::InvalidProgram
    );
    
    let cpi_accounts = Transfer {
        from: ctx.accounts.from.to_account_info(),
        to: ctx.accounts.to.to_account_info(),
        authority: ctx.accounts.authority.to_account_info(),
    };
    
    let cpi_ctx = CpiContext::new(
        ctx.accounts.token_program.to_account_info(),
        cpi_accounts
    );
    
    token::transfer(cpi_ctx, amount)
}
```

## 3. Error Handling and Math Safety

### Custom Error Types

```rust
// programs/my-program/src/error.rs
use anchor_lang::prelude::*;

#[error_code]
pub enum MyProgramError {
    #[msg("Name cannot be empty")]
    InvalidName,
    
    #[msg("Name exceeds maximum length of 50 characters")]
    NameTooLong,
    
    #[msg("Unauthorized: signer is not the authority")]
    Unauthorized,
    
    #[msg("Mathematical operation resulted in overflow")]
    MathOverflow,
    
    #[msg("Invalid program address")]
    InvalidProgram,
    
    #[msg("Insufficient funds for operation")]
    InsufficientFunds,
}

// ✅ Good - Safe math operations
pub fn safe_add(a: u64, b: u64) -> Result<u64> {
    a.checked_add(b).ok_or(MyProgramError::MathOverflow.into())
}

pub fn calculate_interest(principal: u64, rate_bps: u16) -> Result<u64> {
    let interest = principal
        .checked_mul(rate_bps as u64)
        .ok_or(MyProgramError::MathOverflow)?
        .checked_div(10_000)
        .ok_or(MyProgramError::MathOverflow)?;
    Ok(interest)
}
```

## 4. Testing Strategies

### TypeScript Test Setup

```typescript
// tests/my-program.ts
import * as anchor from "@coral-xyz/anchor";
import { Program } from "@coral-xyz/anchor";
import { MyProgram } from "../target/types/my_program";
import { expect } from "chai";

describe("my-program", () => {
  const provider = anchor.AnchorProvider.env();
  anchor.setProvider(provider);
  
  const program = anchor.workspace.MyProgram as Program<MyProgram>;
  const authority = anchor.web3.Keypair.generate();
  
  const [userPda] = anchor.web3.PublicKey.findProgramAddressSync(
    [Buffer.from("user"), authority.publicKey.toBuffer()],
    program.programId
  );
  
  before(async () => {
    await provider.connection.requestAirdrop(
      authority.publicKey,
      2 * anchor.web3.LAMPORTS_PER_SOL
    );
    await new Promise(resolve => setTimeout(resolve, 1000));
  });
  
  it("Should initialize user successfully", async () => {
    const name = "Alice";
    
    const tx = await program.methods
      .initialize(name)
      .accounts({
        user: userPda,
        authority: authority.publicKey,
        systemProgram: anchor.web3.SystemProgram.programId,
      })
      .signers([authority])
      .rpc();
    
    const userAccount = await program.account.user.fetch(userPda);
    expect(userAccount.name).to.equal(name);
    expect(userAccount.authority.toString()).to.equal(authority.publicKey.toString());
  });
  
  it("Should fail with invalid name", async () => {
    const invalidUser = anchor.web3.Keypair.generate();
    const [invalidUserPda] = anchor.web3.PublicKey.findProgramAddressSync(
      [Buffer.from("user"), invalidUser.publicKey.toBuffer()],
      program.programId
    );
    
    try {
      await program.methods
        .initialize("") // Empty name
        .accounts({
          user: invalidUserPda,
          authority: invalidUser.publicKey,
          systemProgram: anchor.web3.SystemProgram.programId,
        })
        .signers([invalidUser])
        .rpc();
      
      expect.fail("Should have thrown an error");
    } catch (error) {
      expect(error.error.errorMessage).to.include("Name cannot be empty");
    }
  });
});
```

## 5. Performance Optimization

### Compute Unit Optimization

```rust
// ✅ Good - Minimize compute usage
pub fn optimized_calculation(data: &[u64]) -> Result<u64> {
    let sum = data
        .iter()
        .take(100) // Limit iterations
        .try_fold(0u64, |acc, &x| {
            acc.checked_add(x).ok_or(MyProgramError::MathOverflow)
        })?;
    Ok(sum)
}

// ✅ Good - Zero-copy for large accounts
#[account(zero_copy)]
#[repr(C)]
pub struct LargeAccount {
    pub data: [u8; 10000],
}

pub fn process_large_account(account: &AccountLoader<LargeAccount>) -> Result<()> {
    let account_data = account.load()?;
    let first_byte = account_data.data[0];
    msg!("First byte: {}", first_byte);
    Ok(())
}

// ✅ Good - Efficient string handling
pub fn process_string(input: &str) -> Result<String> {
    let mut result = String::with_capacity(input.len());
    
    for ch in input.chars().take(50) {
        if ch.is_alphanumeric() {
            result.push(ch.to_ascii_lowercase());
        }
    }
    Ok(result)
}
```

## 6. Development Workflow

### Anchor Configuration

```toml
# Anchor.toml
[features]
seeds = false
skip-lint = false

[programs.localnet]
my_program = "Fg6PaFpoGXkYsidMpWTK6W2BeZ7FEfcYkg476zPFsLnS"

[programs.devnet]
my_program = "Fg6PaFpoGXkYsidMpWTK6W2BeZ7FEfcYkg476zPFsLnS"

[provider]
cluster = "localnet"
wallet = "~/.config/solana/id.json"

[scripts]
test = "yarn run ts-mocha -p ./tsconfig.json -t 1000000 tests/**/*.ts"
```

### Build Scripts

```json
{
  "scripts": {
    "lint": "cargo clippy -- -D warnings",
    "format": "cargo fmt",
    "build": "anchor build",
    "test": "anchor test",
    "deploy-devnet": "anchor deploy --provider.cluster devnet",
    "clean": "anchor clean"
  }
}
```

## 7. Documentation Standards

### Code Documentation

```rust
/// Initialize a new user account with validation
/// 
/// # Arguments
/// * `ctx` - The instruction context containing validated accounts
/// * `name` - The user's display name (max 50 characters)
/// 
/// # Errors
/// * `InvalidName` - If name is empty
/// * `NameTooLong` - If name exceeds 50 characters
pub fn initialize(ctx: Context<Initialize>, name: String) -> Result<()> {
    // Implementation...
}

/// User account state
/// 
/// This account stores user profile information and is created as a PDA
/// using seeds: ["user", authority.key()]
#[account]
pub struct User {
    /// The authority that owns this user account
    pub authority: Pubkey,
    /// User's display name (max 50 chars)
    pub name: String,
    /// Unix timestamp when account was created
    pub created_at: i64,
    /// Unix timestamp of last update
    pub updated_at: i64,
    /// Bump seed used for PDA derivation
    pub bump: u8,
}
```

## 8. AI-Specific Guidelines

### Code Generation Requirements

**WHEN GENERATING RUST/SOLANA CODE:**

- Always use Anchor framework unless specifically requested otherwise
- Include comprehensive account validation with constraint macros
- Generate custom error types for all failure cases
- Add proper documentation with doc comments
- Include corresponding TypeScript tests
- Use safe math operations (checked_add, checked_mul)
- Implement proper PDA derivation with seeds and bumps
- Follow maximum function length of 20 lines, file length of 300 lines

### Security Checklist

**PRE-SUBMISSION VALIDATION:**

- [ ] All accounts validated with appropriate constraints
- [ ] Custom error types defined for all error cases
- [ ] No usage of floating-point types for on-chain data
- [ ] Proper signer verification implemented
- [ ] Safe math operations used throughout
- [ ] CPI calls validate target program IDs
- [ ] Account size calculations are correct
- [ ] Tests cover both success and failure cases
- [ ] Documentation includes security considerations
- [ ] No `panic!()` usage in program code

### Performance Guidelines

**OPTIMIZATION REQUIREMENTS:**

- Use zero-copy deserialization for accounts > 1KB
- Limit compute-intensive operations
- Pre-allocate string capacity when known
- Use iterators instead of manual loops
- Minimize account reallocations
- Profile compute units and optimize bottlenecks

### Common Anti-Patterns to Avoid

**NEVER DO:**

- Use `panic!()` in program code (use `Result<()>` instead)
- Ignore account validation (always use constraints)
- Use floating-point arithmetic for financial calculations
- Hardcode program IDs (use `declare_id!()` macro)
- Skip error handling in CPI calls
- Use unchecked arithmetic operations
- Forget to validate account ownership
- Skip testing edge cases and error conditions
- Use `any` types or unsafe operations without justification
